# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_bollinger.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCsystemathics/apis/services/daily_analytics/v1/daily_bollinger.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x16google/type/date.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\"\xd4\x01\n\x15\x44\x61ilyBollingerRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x0e\n\x06length\x18\x03 \x01(\x05\x12\x11\n\tdeviation\x18\x04 \x01(\x01\x12\x12\n\nadjustment\x18\x05 \x01(\x08\"i\n\x16\x44\x61ilyBollingerResponse\x12O\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x41.systemathics.apis.services.daily_analytics.v1.DailyBollingerData\"\xcc\x01\n\x12\x44\x61ilyBollingerData\x12\x1f\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.Date\x12\r\n\x05value\x18\x02 \x01(\x01\x12+\n\x05lower\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x05upper\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12,\n\x06middle\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue2\xb7\x01\n\x15\x44\x61ilyBollingerService\x12\x9d\x01\n\x0e\x44\x61ilyBollinger\x12\x44.systemathics.apis.services.daily_analytics.v1.DailyBollingerRequest\x1a\x45.systemathics.apis.services.daily_analytics.v1.DailyBollingerResponseb\x06proto3')



_DAILYBOLLINGERREQUEST = DESCRIPTOR.message_types_by_name['DailyBollingerRequest']
_DAILYBOLLINGERRESPONSE = DESCRIPTOR.message_types_by_name['DailyBollingerResponse']
_DAILYBOLLINGERDATA = DESCRIPTOR.message_types_by_name['DailyBollingerData']
DailyBollingerRequest = _reflection.GeneratedProtocolMessageType('DailyBollingerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBOLLINGERREQUEST,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_bollinger_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyBollingerRequest)
  })
_sym_db.RegisterMessage(DailyBollingerRequest)

DailyBollingerResponse = _reflection.GeneratedProtocolMessageType('DailyBollingerResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBOLLINGERRESPONSE,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_bollinger_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyBollingerResponse)
  })
_sym_db.RegisterMessage(DailyBollingerResponse)

DailyBollingerData = _reflection.GeneratedProtocolMessageType('DailyBollingerData', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBOLLINGERDATA,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_bollinger_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyBollingerData)
  })
_sym_db.RegisterMessage(DailyBollingerData)

_DAILYBOLLINGERSERVICE = DESCRIPTOR.services_by_name['DailyBollingerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DAILYBOLLINGERREQUEST._serialized_start=278
  _DAILYBOLLINGERREQUEST._serialized_end=490
  _DAILYBOLLINGERRESPONSE._serialized_start=492
  _DAILYBOLLINGERRESPONSE._serialized_end=597
  _DAILYBOLLINGERDATA._serialized_start=600
  _DAILYBOLLINGERDATA._serialized_end=804
  _DAILYBOLLINGERSERVICE._serialized_start=807
  _DAILYBOLLINGERSERVICE._serialized_end=990
# @@protoc_insertion_point(module_scope)
