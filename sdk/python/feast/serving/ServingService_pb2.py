# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/serving/ServingService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/serving/ServingService.proto',
  package='feast.serving',
  syntax='proto3',
  serialized_options=_b('\n\rfeast.servingB\017ServingAPIProtoZ2github.com/gojek/feast/sdk/go/protos/feast/serving'),
  serialized_pb=_b('\n\"feast/serving/ServingService.proto\x12\rfeast.serving\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17\x66\x65\x61st/types/Value.proto\"\x1f\n\x1dGetFeastServingVersionRequest\"1\n\x1eGetFeastServingVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\"\x1c\n\x1aGetFeastServingTypeRequest\"L\n\x1bGetFeastServingTypeResponse\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.feast.serving.FeastServingType\"\xfd\x03\n\x12GetFeaturesRequest\x12\x42\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32,.feast.serving.GetFeaturesRequest.FeatureSet\x12@\n\x0b\x65ntity_rows\x18\x02 \x03(\x0b\x32+.feast.serving.GetFeaturesRequest.EntityRow\x12!\n\x19omit_entities_in_response\x18\x03 \x01(\x08\x1an\n\nFeatureSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x15\n\rfeature_names\x18\x03 \x03(\t\x12*\n\x07max_age\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x1a\xcd\x01\n\tEntityRow\x12\x34\n\x10\x65ntity_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x37.feast.serving.GetFeaturesRequest.EntityRow.FieldsEntry\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.Value:\x02\x38\x01\"\x8c\x02\n\x19GetOnlineFeaturesResponse\x12J\n\x0c\x66ield_values\x18\x01 \x03(\x0b\x32\x34.feast.serving.GetOnlineFeaturesResponse.FieldValues\x1a\xa2\x01\n\x0b\x46ieldValues\x12P\n\x06\x66ields\x18\x01 \x03(\x0b\x32@.feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.Value:\x02\x38\x01\";\n\x18GetBatchFeaturesResponse\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.feast.serving.Job\"0\n\rGetJobRequest\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.feast.serving.Job\"1\n\x0eGetJobResponse\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.feast.serving.Job\"\xb3\x01\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x04type\x18\x02 \x01(\x0e\x32\x16.feast.serving.JobType\x12(\n\x06status\x18\x03 \x01(\x0e\x32\x18.feast.serving.JobStatus\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\x11\n\tfile_uris\x18\x05 \x03(\t\x12.\n\x0b\x64\x61ta_format\x18\x06 \x01(\x0e\x32\x19.feast.serving.DataFormat*o\n\x10\x46\x65\x61stServingType\x12\x1e\n\x1a\x46\x45\x41ST_SERVING_TYPE_INVALID\x10\x00\x12\x1d\n\x19\x46\x45\x41ST_SERVING_TYPE_ONLINE\x10\x01\x12\x1c\n\x18\x46\x45\x41ST_SERVING_TYPE_BATCH\x10\x02*6\n\x07JobType\x12\x14\n\x10JOB_TYPE_INVALID\x10\x00\x12\x15\n\x11JOB_TYPE_DOWNLOAD\x10\x01*h\n\tJobStatus\x12\x16\n\x12JOB_STATUS_INVALID\x10\x00\x12\x16\n\x12JOB_STATUS_PENDING\x10\x01\x12\x16\n\x12JOB_STATUS_RUNNING\x10\x02\x12\x13\n\x0fJOB_STATUS_DONE\x10\x03*\x7f\n\nDataFormat\x12\x17\n\x13\x44\x41TA_FORMAT_INVALID\x10\x00\x12\x13\n\x0f\x44\x41TA_FORMAT_CSV\x10\x01\x12\x17\n\x13\x44\x41TA_FORMAT_PARQUET\x10\x02\x12\x14\n\x10\x44\x41TA_FORMAT_AVRO\x10\x03\x12\x14\n\x10\x44\x41TA_FORMAT_JSON\x10\x04\x32\xfe\x03\n\x0eServingService\x12u\n\x16GetFeastServingVersion\x12,.feast.serving.GetFeastServingVersionRequest\x1a-.feast.serving.GetFeastServingVersionResponse\x12l\n\x13GetFeastServingType\x12).feast.serving.GetFeastServingTypeRequest\x1a*.feast.serving.GetFeastServingTypeResponse\x12`\n\x11GetOnlineFeatures\x12!.feast.serving.GetFeaturesRequest\x1a(.feast.serving.GetOnlineFeaturesResponse\x12^\n\x10GetBatchFeatures\x12!.feast.serving.GetFeaturesRequest\x1a\'.feast.serving.GetBatchFeaturesResponse\x12\x45\n\x06GetJob\x12\x1c.feast.serving.GetJobRequest\x1a\x1d.feast.serving.GetJobResponseBT\n\rfeast.servingB\x0fServingAPIProtoZ2github.com/gojek/feast/sdk/go/protos/feast/servingb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,feast_dot_types_dot_Value__pb2.DESCRIPTOR,])

_FEASTSERVINGTYPE = _descriptor.EnumDescriptor(
  name='FeastServingType',
  full_name='feast.serving.FeastServingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_ONLINE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_BATCH', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1462,
  serialized_end=1573,
)
_sym_db.RegisterEnumDescriptor(_FEASTSERVINGTYPE)

FeastServingType = enum_type_wrapper.EnumTypeWrapper(_FEASTSERVINGTYPE)
_JOBTYPE = _descriptor.EnumDescriptor(
  name='JobType',
  full_name='feast.serving.JobType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOB_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_TYPE_DOWNLOAD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1575,
  serialized_end=1629,
)
_sym_db.RegisterEnumDescriptor(_JOBTYPE)

JobType = enum_type_wrapper.EnumTypeWrapper(_JOBTYPE)
_JOBSTATUS = _descriptor.EnumDescriptor(
  name='JobStatus',
  full_name='feast.serving.JobStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB_STATUS_DONE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1631,
  serialized_end=1735,
)
_sym_db.RegisterEnumDescriptor(_JOBSTATUS)

JobStatus = enum_type_wrapper.EnumTypeWrapper(_JOBSTATUS)
_DATAFORMAT = _descriptor.EnumDescriptor(
  name='DataFormat',
  full_name='feast.serving.DataFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA_FORMAT_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_FORMAT_CSV', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_FORMAT_PARQUET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_FORMAT_AVRO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_FORMAT_JSON', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1737,
  serialized_end=1864,
)
_sym_db.RegisterEnumDescriptor(_DATAFORMAT)

DataFormat = enum_type_wrapper.EnumTypeWrapper(_DATAFORMAT)
FEAST_SERVING_TYPE_INVALID = 0
FEAST_SERVING_TYPE_ONLINE = 1
FEAST_SERVING_TYPE_BATCH = 2
JOB_TYPE_INVALID = 0
JOB_TYPE_DOWNLOAD = 1
JOB_STATUS_INVALID = 0
JOB_STATUS_PENDING = 1
JOB_STATUS_RUNNING = 2
JOB_STATUS_DONE = 3
DATA_FORMAT_INVALID = 0
DATA_FORMAT_CSV = 1
DATA_FORMAT_PARQUET = 2
DATA_FORMAT_AVRO = 3
DATA_FORMAT_JSON = 4



_GETFEASTSERVINGVERSIONREQUEST = _descriptor.Descriptor(
  name='GetFeastServingVersionRequest',
  full_name='feast.serving.GetFeastServingVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=174,
)


_GETFEASTSERVINGVERSIONRESPONSE = _descriptor.Descriptor(
  name='GetFeastServingVersionResponse',
  full_name='feast.serving.GetFeastServingVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.serving.GetFeastServingVersionResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=225,
)


_GETFEASTSERVINGTYPEREQUEST = _descriptor.Descriptor(
  name='GetFeastServingTypeRequest',
  full_name='feast.serving.GetFeastServingTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=255,
)


_GETFEASTSERVINGTYPERESPONSE = _descriptor.Descriptor(
  name='GetFeastServingTypeResponse',
  full_name='feast.serving.GetFeastServingTypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.serving.GetFeastServingTypeResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=333,
)


_GETFEATURESREQUEST_FEATURESET = _descriptor.Descriptor(
  name='FeatureSet',
  full_name='feast.serving.GetFeaturesRequest.FeatureSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.serving.GetFeaturesRequest.FeatureSet.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.serving.GetFeaturesRequest.FeatureSet.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_names', full_name='feast.serving.GetFeaturesRequest.FeatureSet.feature_names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_age', full_name='feast.serving.GetFeaturesRequest.FeatureSet.max_age', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=637,
)

_GETFEATURESREQUEST_ENTITYROW_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='feast.serving.GetFeaturesRequest.EntityRow.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetFeaturesRequest.EntityRow.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetFeaturesRequest.EntityRow.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=780,
  serialized_end=845,
)

_GETFEATURESREQUEST_ENTITYROW = _descriptor.Descriptor(
  name='EntityRow',
  full_name='feast.serving.GetFeaturesRequest.EntityRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_timestamp', full_name='feast.serving.GetFeaturesRequest.EntityRow.entity_timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='feast.serving.GetFeaturesRequest.EntityRow.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETFEATURESREQUEST_ENTITYROW_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=845,
)

_GETFEATURESREQUEST = _descriptor.Descriptor(
  name='GetFeaturesRequest',
  full_name='feast.serving.GetFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_sets', full_name='feast.serving.GetFeaturesRequest.feature_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity_rows', full_name='feast.serving.GetFeaturesRequest.entity_rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='omit_entities_in_response', full_name='feast.serving.GetFeaturesRequest.omit_entities_in_response', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETFEATURESREQUEST_FEATURESET, _GETFEATURESREQUEST_ENTITYROW, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=845,
)


_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=780,
  serialized_end=845,
)

_GETONLINEFEATURESRESPONSE_FIELDVALUES = _descriptor.Descriptor(
  name='FieldValues',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=954,
  serialized_end=1116,
)

_GETONLINEFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetOnlineFeaturesResponse',
  full_name='feast.serving.GetOnlineFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_values', full_name='feast.serving.GetOnlineFeaturesResponse.field_values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESRESPONSE_FIELDVALUES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=848,
  serialized_end=1116,
)


_GETBATCHFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetBatchFeaturesResponse',
  full_name='feast.serving.GetBatchFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='feast.serving.GetBatchFeaturesResponse.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1118,
  serialized_end=1177,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='feast.serving.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='feast.serving.GetJobRequest.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1179,
  serialized_end=1227,
)


_GETJOBRESPONSE = _descriptor.Descriptor(
  name='GetJobResponse',
  full_name='feast.serving.GetJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='feast.serving.GetJobResponse.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1229,
  serialized_end=1278,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='feast.serving.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.serving.Job.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.serving.Job.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='feast.serving.Job.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='feast.serving.Job.error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_uris', full_name='feast.serving.Job.file_uris', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_format', full_name='feast.serving.Job.data_format', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1281,
  serialized_end=1460,
)

_GETFEASTSERVINGTYPERESPONSE.fields_by_name['type'].enum_type = _FEASTSERVINGTYPE
_GETFEATURESREQUEST_FEATURESET.fields_by_name['max_age'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_GETFEATURESREQUEST_FEATURESET.containing_type = _GETFEATURESREQUEST
_GETFEATURESREQUEST_ENTITYROW_FIELDSENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETFEATURESREQUEST_ENTITYROW_FIELDSENTRY.containing_type = _GETFEATURESREQUEST_ENTITYROW
_GETFEATURESREQUEST_ENTITYROW.fields_by_name['entity_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETFEATURESREQUEST_ENTITYROW.fields_by_name['fields'].message_type = _GETFEATURESREQUEST_ENTITYROW_FIELDSENTRY
_GETFEATURESREQUEST_ENTITYROW.containing_type = _GETFEATURESREQUEST
_GETFEATURESREQUEST.fields_by_name['feature_sets'].message_type = _GETFEATURESREQUEST_FEATURESET
_GETFEATURESREQUEST.fields_by_name['entity_rows'].message_type = _GETFEATURESREQUEST_ENTITYROW
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY.containing_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES
_GETONLINEFEATURESRESPONSE_FIELDVALUES.fields_by_name['fields'].message_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY
_GETONLINEFEATURESRESPONSE_FIELDVALUES.containing_type = _GETONLINEFEATURESRESPONSE
_GETONLINEFEATURESRESPONSE.fields_by_name['field_values'].message_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES
_GETBATCHFEATURESRESPONSE.fields_by_name['job'].message_type = _JOB
_GETJOBREQUEST.fields_by_name['job'].message_type = _JOB
_GETJOBRESPONSE.fields_by_name['job'].message_type = _JOB
_JOB.fields_by_name['type'].enum_type = _JOBTYPE
_JOB.fields_by_name['status'].enum_type = _JOBSTATUS
_JOB.fields_by_name['data_format'].enum_type = _DATAFORMAT
DESCRIPTOR.message_types_by_name['GetFeastServingVersionRequest'] = _GETFEASTSERVINGVERSIONREQUEST
DESCRIPTOR.message_types_by_name['GetFeastServingVersionResponse'] = _GETFEASTSERVINGVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['GetFeastServingTypeRequest'] = _GETFEASTSERVINGTYPEREQUEST
DESCRIPTOR.message_types_by_name['GetFeastServingTypeResponse'] = _GETFEASTSERVINGTYPERESPONSE
DESCRIPTOR.message_types_by_name['GetFeaturesRequest'] = _GETFEATURESREQUEST
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesResponse'] = _GETONLINEFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetBatchFeaturesResponse'] = _GETBATCHFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobResponse'] = _GETJOBRESPONSE
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.enum_types_by_name['FeastServingType'] = _FEASTSERVINGTYPE
DESCRIPTOR.enum_types_by_name['JobType'] = _JOBTYPE
DESCRIPTOR.enum_types_by_name['JobStatus'] = _JOBSTATUS
DESCRIPTOR.enum_types_by_name['DataFormat'] = _DATAFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeastServingVersionRequest = _reflection.GeneratedProtocolMessageType('GetFeastServingVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGVERSIONREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingVersionRequest)
  })
_sym_db.RegisterMessage(GetFeastServingVersionRequest)

GetFeastServingVersionResponse = _reflection.GeneratedProtocolMessageType('GetFeastServingVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGVERSIONRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingVersionResponse)
  })
_sym_db.RegisterMessage(GetFeastServingVersionResponse)

GetFeastServingTypeRequest = _reflection.GeneratedProtocolMessageType('GetFeastServingTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGTYPEREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingTypeRequest)
  })
_sym_db.RegisterMessage(GetFeastServingTypeRequest)

GetFeastServingTypeResponse = _reflection.GeneratedProtocolMessageType('GetFeastServingTypeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGTYPERESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingTypeResponse)
  })
_sym_db.RegisterMessage(GetFeastServingTypeResponse)

GetFeaturesRequest = _reflection.GeneratedProtocolMessageType('GetFeaturesRequest', (_message.Message,), {

  'FeatureSet' : _reflection.GeneratedProtocolMessageType('FeatureSet', (_message.Message,), {
    'DESCRIPTOR' : _GETFEATURESREQUEST_FEATURESET,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetFeaturesRequest.FeatureSet)
    })
  ,

  'EntityRow' : _reflection.GeneratedProtocolMessageType('EntityRow', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETFEATURESREQUEST_ENTITYROW_FIELDSENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetFeaturesRequest.EntityRow.FieldsEntry)
      })
    ,
    'DESCRIPTOR' : _GETFEATURESREQUEST_ENTITYROW,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetFeaturesRequest.EntityRow)
    })
  ,
  'DESCRIPTOR' : _GETFEATURESREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeaturesRequest)
  })
_sym_db.RegisterMessage(GetFeaturesRequest)
_sym_db.RegisterMessage(GetFeaturesRequest.FeatureSet)
_sym_db.RegisterMessage(GetFeaturesRequest.EntityRow)
_sym_db.RegisterMessage(GetFeaturesRequest.EntityRow.FieldsEntry)

GetOnlineFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesResponse', (_message.Message,), {

  'FieldValues' : _reflection.GeneratedProtocolMessageType('FieldValues', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry)
      })
    ,
    'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FIELDVALUES,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FieldValues)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesResponse)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FieldValues)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FieldValues.FieldsEntry)

GetBatchFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetBatchFeaturesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBATCHFEATURESRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetBatchFeaturesResponse)
  })
_sym_db.RegisterMessage(GetBatchFeaturesResponse)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

GetJobResponse = _reflection.GeneratedProtocolMessageType('GetJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetJobResponse)
  })
_sym_db.RegisterMessage(GetJobResponse)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.Job)
  })
_sym_db.RegisterMessage(Job)


DESCRIPTOR._options = None
_GETFEATURESREQUEST_ENTITYROW_FIELDSENTRY._options = None
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY._options = None

_SERVINGSERVICE = _descriptor.ServiceDescriptor(
  name='ServingService',
  full_name='feast.serving.ServingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1867,
  serialized_end=2377,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeastServingVersion',
    full_name='feast.serving.ServingService.GetFeastServingVersion',
    index=0,
    containing_service=None,
    input_type=_GETFEASTSERVINGVERSIONREQUEST,
    output_type=_GETFEASTSERVINGVERSIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFeastServingType',
    full_name='feast.serving.ServingService.GetFeastServingType',
    index=1,
    containing_service=None,
    input_type=_GETFEASTSERVINGTYPEREQUEST,
    output_type=_GETFEASTSERVINGTYPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetOnlineFeatures',
    full_name='feast.serving.ServingService.GetOnlineFeatures',
    index=2,
    containing_service=None,
    input_type=_GETFEATURESREQUEST,
    output_type=_GETONLINEFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBatchFeatures',
    full_name='feast.serving.ServingService.GetBatchFeatures',
    index=3,
    containing_service=None,
    input_type=_GETFEATURESREQUEST,
    output_type=_GETBATCHFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='feast.serving.ServingService.GetJob',
    index=4,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_GETJOBRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVINGSERVICE)

DESCRIPTOR.services_by_name['ServingService'] = _SERVINGSERVICE

# @@protoc_insertion_point(module_scope)
