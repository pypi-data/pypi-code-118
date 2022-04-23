# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_rsi.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=systemathics/apis/services/daily_analytics/v1/daily_rsi.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\"\xbb\x01\n\x0f\x44\x61ilyRsiRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x0e\n\x06length\x18\x03 \x01(\x05\x12\x12\n\nadjustment\x18\x04 \x01(\x08\"]\n\x10\x44\x61ilyRsiResponse\x12I\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32;.systemathics.apis.services.daily_analytics.v1.DailyRsiData\"K\n\x0c\x44\x61ilyRsiData\x12\x1f\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.Date\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x0b\n\x03rsi\x18\x03 \x01(\x01\x32\x9f\x01\n\x0f\x44\x61ilyRsiService\x12\x8b\x01\n\x08\x44\x61ilyRsi\x12>.systemathics.apis.services.daily_analytics.v1.DailyRsiRequest\x1a?.systemathics.apis.services.daily_analytics.v1.DailyRsiResponseb\x06proto3')



_DAILYRSIREQUEST = DESCRIPTOR.message_types_by_name['DailyRsiRequest']
_DAILYRSIRESPONSE = DESCRIPTOR.message_types_by_name['DailyRsiResponse']
_DAILYRSIDATA = DESCRIPTOR.message_types_by_name['DailyRsiData']
DailyRsiRequest = _reflection.GeneratedProtocolMessageType('DailyRsiRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYRSIREQUEST,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_rsi_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyRsiRequest)
  })
_sym_db.RegisterMessage(DailyRsiRequest)

DailyRsiResponse = _reflection.GeneratedProtocolMessageType('DailyRsiResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYRSIRESPONSE,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_rsi_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyRsiResponse)
  })
_sym_db.RegisterMessage(DailyRsiResponse)

DailyRsiData = _reflection.GeneratedProtocolMessageType('DailyRsiData', (_message.Message,), {
  'DESCRIPTOR' : _DAILYRSIDATA,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_rsi_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyRsiData)
  })
_sym_db.RegisterMessage(DailyRsiData)

_DAILYRSISERVICE = DESCRIPTOR.services_by_name['DailyRsiService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DAILYRSIREQUEST._serialized_start=240
  _DAILYRSIREQUEST._serialized_end=427
  _DAILYRSIRESPONSE._serialized_start=429
  _DAILYRSIRESPONSE._serialized_end=522
  _DAILYRSIDATA._serialized_start=524
  _DAILYRSIDATA._serialized_end=599
  _DAILYRSISERVICE._serialized_start=602
  _DAILYRSISERVICE._serialized_end=761
# @@protoc_insertion_point(module_scope)
