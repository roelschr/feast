package main

import (
	"context"
	"net"
	"os"
	"path/filepath"
	"reflect"
	"runtime"
	"testing"
	"time"

	"github.com/feast-dev/feast/go/internal/feast/registry"

	"github.com/apache/arrow/go/v8/arrow/array"
	"github.com/apache/arrow/go/v8/arrow/memory"
	"github.com/apache/arrow/go/v8/parquet/file"
	"github.com/apache/arrow/go/v8/parquet/pqarrow"
	"github.com/feast-dev/feast/go/cmd/server/logging"
	"github.com/feast-dev/feast/go/internal/feast"
	"github.com/feast-dev/feast/go/internal/test"
	"github.com/feast-dev/feast/go/protos/feast/serving"
	"github.com/feast-dev/feast/go/protos/feast/types"
	"github.com/stretchr/testify/assert"
	"google.golang.org/grpc"
	"google.golang.org/grpc/test/bufconn"
)

// Return absolute path to the test_repo directory regardless of the working directory
func getRepoPath(basePath string) string {
	// Get the file path of this source file, regardless of the working directory
	if basePath == "" {
		_, filename, _, ok := runtime.Caller(0)
		if !ok {
			panic("couldn't find file path of the test file")
		}
		return filepath.Join(filename, "..", "..", "feature_repo")
	} else {
		return filepath.Join(basePath, "feature_repo")
	}
}

// Starts a new grpc server, registers the serving service and returns a client.
func getClient(ctx context.Context, offlineStoreType string, basePath string, enableLogging bool) (serving.ServingServiceClient, func()) {
	buffer := 1024 * 1024
	listener := bufconn.Listen(buffer)

	server := grpc.NewServer()
	config, err := registry.NewRepoConfigFromFile(getRepoPath(basePath))

	// TODO(kevjumba): either add this officially or talk in design review about what the correct solution for what do with path.
	// Currently in python we use the path in FileSource but it is not specified in configuration unless it is using file_url?
	if enableLogging {
		if config.OfflineStore == nil {
			config.OfflineStore = map[string]interface{}{}
		}
		absPath, err := filepath.Abs(filepath.Join(getRepoPath(basePath), "log.parquet"))
		if err != nil {
			panic(err)
		}
		config.OfflineStore["path"] = absPath
		config.OfflineStore["storeType"] = offlineStoreType
	}

	if err != nil {
		panic(err)
	}
	fs, err := feast.NewFeatureStore(config, nil)
	if err != nil {
		panic(err)
	}
	loggingService, err := logging.NewLoggingService(fs, 1000, "test_service", enableLogging)
	if err != nil {
		panic(err)
	}
	servingServiceServer := newServingServiceServer(fs, loggingService)

	serving.RegisterServingServiceServer(server, servingServiceServer)
	go func() {
		if err := server.Serve(listener); err != nil {
			panic(err)
		}
	}()

	conn, _ := grpc.DialContext(ctx, "", grpc.WithContextDialer(func(context.Context, string) (net.Conn, error) {
		return listener.Dial()
	}), grpc.WithInsecure())

	closer := func() {
		listener.Close()
		server.Stop()
	}

	client := serving.NewServingServiceClient(conn)

	return client, closer
}

func TestGetFeastServingInfo(t *testing.T) {
	ctx := context.Background()
	// Pregenerated using `feast init`.
	dir := "logging/"
	err := test.SetupInitializedRepo(dir)
	assert.Nil(t, err)
	defer test.CleanUpInitializedRepo(dir)

	client, closer := getClient(ctx, "", dir, false)
	defer closer()
	response, err := client.GetFeastServingInfo(ctx, &serving.GetFeastServingInfoRequest{})
	assert.Nil(t, err)
	assert.Equal(t, feastServerVersion, response.Version)
}

func TestGetOnlineFeaturesSqlite(t *testing.T) {
	ctx := context.Background()
	// Pregenerated using `feast init`.
	dir := "logging/"
	err := test.SetupInitializedRepo(dir)
	assert.Nil(t, err)
	defer test.CleanUpInitializedRepo(dir)

	client, closer := getClient(ctx, "", dir, false)
	defer closer()
	entities := make(map[string]*types.RepeatedValue)
	entities["driver_id"] = &types.RepeatedValue{
		Val: []*types.Value{
			{Val: &types.Value_Int64Val{Int64Val: 1001}},
			{Val: &types.Value_Int64Val{Int64Val: 1003}},
			{Val: &types.Value_Int64Val{Int64Val: 1005}},
		},
	}
	request := &serving.GetOnlineFeaturesRequest{
		Kind: &serving.GetOnlineFeaturesRequest_Features{
			Features: &serving.FeatureList{
				Val: []string{"driver_hourly_stats:conv_rate", "driver_hourly_stats:acc_rate", "driver_hourly_stats:avg_daily_trips"},
			},
		},
		Entities: entities,
	}
	response, err := client.GetOnlineFeatures(ctx, request)
	assert.Nil(t, err)
	assert.NotNil(t, response)
	expectedEntityValuesResp := []*types.Value{
		{Val: &types.Value_Int64Val{Int64Val: 1001}},
		{Val: &types.Value_Int64Val{Int64Val: 1003}},
		{Val: &types.Value_Int64Val{Int64Val: 1005}},
	}
	expectedFeatureNamesResp := []string{"driver_id", "conv_rate", "acc_rate", "avg_daily_trips"}
	rows, err := test.ReadParquet(filepath.Join(dir, "feature_repo", "driver_stats.parquet"))
	assert.Nil(t, err)
	entityKeys := map[int64]bool{1001: true, 1003: true, 1005: true}
	correctFeatures := test.GetLatestFeatures(rows, entityKeys)
	expectedConvRateValues := []*types.Value{}
	expectedAccRateValues := []*types.Value{}
	expectedAvgDailyTripsValues := []*types.Value{}

	for _, key := range []int64{1001, 1003, 1005} {
		expectedConvRateValues = append(expectedConvRateValues, &types.Value{Val: &types.Value_FloatVal{FloatVal: correctFeatures[key].ConvRate}})
		expectedAccRateValues = append(expectedAccRateValues, &types.Value{Val: &types.Value_FloatVal{FloatVal: correctFeatures[key].AccRate}})
		expectedAvgDailyTripsValues = append(expectedAvgDailyTripsValues, &types.Value{Val: &types.Value_Int64Val{Int64Val: int64(correctFeatures[key].AvgDailyTrips)}})
	}
	// Columnar so get in column format row by row should have column names of all features
	assert.Equal(t, len(response.Results), 4)

	assert.True(t, reflect.DeepEqual(response.Results[0].Values, expectedEntityValuesResp))
	assert.True(t, reflect.DeepEqual(response.Results[1].Values, expectedConvRateValues))
	assert.True(t, reflect.DeepEqual(response.Results[2].Values, expectedAccRateValues))
	assert.True(t, reflect.DeepEqual(response.Results[3].Values, expectedAvgDailyTripsValues))

	assert.True(t, reflect.DeepEqual(response.Metadata.FeatureNames.Val, expectedFeatureNamesResp))
}

func TestGetOnlineFeaturesSqliteWithLogging(t *testing.T) {
	ctx := context.Background()
	// Pregenerated using `feast init`.
	dir := "logging/"
	err := test.SetupInitializedRepo(dir)
	assert.Nil(t, err)
	defer test.CleanUpInitializedRepo(dir)

	client, closer := getClient(ctx, "file", dir, true)
	defer closer()
	entities := make(map[string]*types.RepeatedValue)
	entities["driver_id"] = &types.RepeatedValue{
		Val: []*types.Value{
			{Val: &types.Value_Int64Val{Int64Val: 1001}},
			{Val: &types.Value_Int64Val{Int64Val: 1003}},
			{Val: &types.Value_Int64Val{Int64Val: 1005}},
		},
	}

	request := &serving.GetOnlineFeaturesRequest{
		Kind: &serving.GetOnlineFeaturesRequest_FeatureService{
			FeatureService: "test_service",
		},
		Entities:         entities,
		FullFeatureNames: true,
	}
	response, err := client.GetOnlineFeatures(ctx, request)

	assert.Nil(t, err)
	assert.NotNil(t, response)

	// Get the featurenames without the entity names that are appended at the front.
	featureNames := response.Metadata.FeatureNames.Val[len(request.Entities):]
	// Generated expected log rows and values
	// TODO(kevjumba): implement for timestamp and status
	expectedLogValues, _, _ := GetExpectedLogRows(featureNames, response.Results[len(request.Entities):])
	expectedLogValues["driver_id"] = entities["driver_id"]
	logPath, err := filepath.Abs(filepath.Join(dir, "feature_repo", "log.parquet"))
	// Wait for logger to flush.
	assert.Eventually(t, func() bool {
		var _, err = os.Stat(logPath)
		if os.IsNotExist(err) {
			return false
		} else {
			return true
		}
	}, 1*time.Second, logging.DEFAULT_LOG_FLUSH_INTERVAL)
	assert.Nil(t, err)
	pf, err := file.OpenParquetFile(logPath, false)
	assert.Nil(t, err)

	reader, err := pqarrow.NewFileReader(pf, pqarrow.ArrowReadProperties{}, memory.DefaultAllocator)
	assert.Nil(t, err)

	tbl, err := reader.ReadTable(ctx)
	assert.Nil(t, err)
	tr := array.NewTableReader(tbl, -1)
	defer tbl.Release()
	defer tr.Release()
	for tr.Next() {
		rec := tr.Record()
		assert.NotNil(t, rec)
		values, err := test.GetProtoFromRecord(rec)

		assert.Nil(t, err)
		assert.Equal(t, len(values)-1 /*request id column not counted*/, len(expectedLogValues))
		// Need to iterate through and compare because certain values in types.RepeatedValues aren't accurately being compared.
		for name, val := range values {
			if name == "RequestId" {
				// Ensure there are request ids for each entity.
				assert.Equal(t, len(val.Val), len(response.Results[0].Values))
			} else {
				assert.Equal(t, len(val.Val), len(expectedLogValues[name].Val))
				for idx, featureVal := range val.Val {
					assert.Equal(t, featureVal.Val, expectedLogValues[name].Val[idx].Val)
				}
			}

		}
	}
	err = test.CleanUpFile(logPath)
	assert.Nil(t, err)
}

// Generate the expected log rows based on the resulting feature vector returned from GetOnlineFeatures.
func GetExpectedLogRows(featureNames []string, results []*serving.GetOnlineFeaturesResponse_FeatureVector) (map[string]*types.RepeatedValue, [][]int32, [][]int64) {
	numFeatures := len(featureNames)
	numRows := len(results[0].Values)
	featureValueLogRows := make(map[string]*types.RepeatedValue)
	featureStatusLogRows := make([][]int32, numRows)
	eventTimestampLogRows := make([][]int64, numRows)
	for idx := 0; idx < len(results); idx++ {
		valArray := make([]*types.Value, 0)
		for row_idx := 0; row_idx < numRows; row_idx++ {
			featureStatusLogRows[row_idx] = make([]int32, numFeatures)
			eventTimestampLogRows[row_idx] = make([]int64, numFeatures)
			valArray = append(valArray, results[idx].Values[row_idx])
			featureStatusLogRows[row_idx][idx] = int32(serving.FieldStatus_PRESENT)
			eventTimestampLogRows[row_idx][idx] = results[idx].EventTimestamps[row_idx].AsTime().UnixNano() / int64(time.Millisecond)

		}
		featureValueLogRows[featureNames[idx]] = &types.RepeatedValue{
			Val: valArray,
		}
	}
	return featureValueLogRows, featureStatusLogRows, eventTimestampLogRows
}
