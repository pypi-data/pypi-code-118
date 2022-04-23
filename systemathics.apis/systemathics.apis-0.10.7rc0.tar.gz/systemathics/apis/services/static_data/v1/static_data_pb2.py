# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/static_data/v1/static_data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;systemathics/apis/services/static_data/v1/static_data.proto\x12)systemathics.apis.services.static_data.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\"\xbb\x04\n\x11StaticDataRequest\x12H\n\nasset_type\x18\x01 \x01(\x0e\x32\x34.systemathics.apis.services.static_data.v1.AssetType\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x65xchange\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06ticker\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0f\x66uture_contract\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0f\x66uture_category\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\requity_sector\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05index\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04\x63ode\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x05start\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12*\n\x05\x63ount\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"\xb2\x02\n\x12StaticDataResponse\x12G\n\x07\x66utures\x18\x01 \x03(\x0b\x32\x36.systemathics.apis.services.static_data.v1.FutureEntry\x12H\n\x08\x65quities\x18\x02 \x03(\x0b\x32\x36.systemathics.apis.services.static_data.v1.EquityEntry\x12\x41\n\x04\x65tfs\x18\x03 \x03(\x0b\x32\x33.systemathics.apis.services.static_data.v1.EtfEntry\x12\x46\n\x07indices\x18\x04 \x03(\x0b\x32\x35.systemathics.apis.services.static_data.v1.IndexEntry\"\x93\x08\n\x0b\x45quityEntry\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07primary\x18\x03 \x01(\t\x12\x11\n\toperating\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08\x63urrency\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12K\n\x0etick_size_rule\x18\x08 \x03(\x0b\x32\x33.systemathics.apis.services.static_data.v1.TickSize\x12\r\n\x05index\x18\t \x03(\t\x12\x0c\n\x04open\x18\n \x01(\t\x12\r\n\x05\x63lose\x18\x0b \x01(\t\x12\x11\n\ttime_zone\x18\x0c \x01(\t\x12\x10\n\x08lot_size\x18\r \x01(\x03\x12\x13\n\x0bpoint_value\x18\x0e \x01(\x01\x12+\n\x05price\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x06volume\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x1f\n\x04time\x18\x11 \x01(\x0b\x32\x11.google.type.Date\x12\x0f\n\x07sources\x18\x12 \x01(\x05\x12T\n\x07mapping\x18\x13 \x03(\x0b\x32\x43.systemathics.apis.services.static_data.v1.EquityEntry.MappingEntry\x12\x11\n\tbloomberg\x18\x14 \x01(\t\x12\x0f\n\x07reuters\x18\x15 \x01(\t\x12\x13\n\x0bmorningstar\x18\x16 \x01(\t\x12\x0c\n\x04\x66igi\x18\x17 \x01(\t\x12\r\n\x05\x66igic\x18\x18 \x01(\t\x12\x0c\n\x04isin\x18\x19 \x01(\t\x12\r\n\x05\x63usip\x18\x1a \x01(\t\x12\r\n\x05sedol\x18\x1b \x01(\t\x12\x0b\n\x03\x63ik\x18\x1c \x01(\t\x12T\n\x07sectors\x18\x1d \x03(\x0b\x32\x43.systemathics.apis.services.static_data.v1.EquityEntry.SectorsEntry\x12\x34\n\x0e\x63\x61pitalization\x18\x1e \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x13\n\x0b\x64\x65scription\x18\x1f \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18  \x01(\t\x12\r\n\x05phone\x18! \x01(\t\x12\r\n\x05\x65mail\x18\" \x01(\t\x12\x0b\n\x03url\x18# \x01(\t\x1a.\n\x0cMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0cSectorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8a\x08\n\x08\x45tfEntry\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07primary\x18\x03 \x01(\t\x12\x11\n\toperating\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08\x63urrency\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12K\n\x0etick_size_rule\x18\x08 \x03(\x0b\x32\x33.systemathics.apis.services.static_data.v1.TickSize\x12\r\n\x05index\x18\t \x03(\t\x12\x0c\n\x04open\x18\n \x01(\t\x12\r\n\x05\x63lose\x18\x0b \x01(\t\x12\x11\n\ttime_zone\x18\x0c \x01(\t\x12\x10\n\x08lot_size\x18\r \x01(\x03\x12\x13\n\x0bpoint_value\x18\x0e \x01(\x01\x12+\n\x05price\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x06volume\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x1f\n\x04time\x18\x11 \x01(\x0b\x32\x11.google.type.Date\x12\x0f\n\x07sources\x18\x12 \x01(\x05\x12Q\n\x07mapping\x18\x13 \x03(\x0b\x32@.systemathics.apis.services.static_data.v1.EtfEntry.MappingEntry\x12\x11\n\tbloomberg\x18\x14 \x01(\t\x12\x0f\n\x07reuters\x18\x15 \x01(\t\x12\x13\n\x0bmorningstar\x18\x16 \x01(\t\x12\x0c\n\x04\x66igi\x18\x17 \x01(\t\x12\r\n\x05\x66igic\x18\x18 \x01(\t\x12\x0c\n\x04isin\x18\x19 \x01(\t\x12\r\n\x05\x63usip\x18\x1a \x01(\t\x12\r\n\x05sedol\x18\x1b \x01(\t\x12\x0b\n\x03\x63ik\x18\x1c \x01(\t\x12Q\n\x07sectors\x18\x1d \x03(\x0b\x32@.systemathics.apis.services.static_data.v1.EtfEntry.SectorsEntry\x12\x34\n\x0e\x63\x61pitalization\x18\x1e \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x13\n\x0b\x64\x65scription\x18\x1f \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18  \x01(\t\x12\r\n\x05phone\x18! \x01(\t\x12\r\n\x05\x65mail\x18\" \x01(\t\x12\x0b\n\x03url\x18# \x01(\t\x1a.\n\x0cMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0cSectorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcd\x07\n\x0b\x46utureEntry\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07primary\x18\x03 \x01(\t\x12\x11\n\toperating\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08\x63urrency\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12K\n\x0etick_size_rule\x18\x08 \x03(\x0b\x32\x33.systemathics.apis.services.static_data.v1.TickSize\x12\r\n\x05index\x18\t \x03(\t\x12\x0c\n\x04open\x18\n \x01(\t\x12\r\n\x05\x63lose\x18\x0b \x01(\t\x12\x11\n\ttime_zone\x18\x0c \x01(\t\x12\x10\n\x08lot_size\x18\r \x01(\x03\x12\x13\n\x0bpoint_value\x18\x0e \x01(\x01\x12+\n\x05price\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x06volume\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x1f\n\x04time\x18\x11 \x01(\x0b\x32\x11.google.type.Date\x12\x0f\n\x07sources\x18\x12 \x01(\x05\x12T\n\x07mapping\x18\x13 \x03(\x0b\x32\x43.systemathics.apis.services.static_data.v1.FutureEntry.MappingEntry\x12\x11\n\tbloomberg\x18\x14 \x01(\t\x12\x0f\n\x07reuters\x18\x15 \x01(\t\x12\x13\n\x0bmorningstar\x18\x16 \x01(\t\x12\x0c\n\x04\x66igi\x18\x17 \x01(\t\x12\r\n\x05\x66igic\x18\x18 \x01(\t\x12\x12\n\nunderlying\x18\x19 \x01(\t\x12\x10\n\x08\x63ontract\x18\x1a \x01(\t\x12V\n\x08\x63\x61tegory\x18\x1b \x03(\x0b\x32\x44.systemathics.apis.services.static_data.v1.FutureEntry.CategoryEntry\x12\r\n\x05\x63hain\x18\x1c \x01(\t\x12#\n\x08maturity\x18\x1d \x01(\x0b\x32\x11.google.type.Date\x12\r\n\x05month\x18\x1e \x01(\t\x12\x0c\n\x04year\x18\x1f \x01(\x05\x1a.\n\x0cMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rCategoryEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe0\x05\n\nIndexEntry\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07primary\x18\x03 \x01(\t\x12\x11\n\toperating\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08\x63urrency\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12K\n\x0etick_size_rule\x18\x08 \x03(\x0b\x32\x33.systemathics.apis.services.static_data.v1.TickSize\x12\r\n\x05index\x18\t \x03(\t\x12\x0c\n\x04open\x18\n \x01(\t\x12\r\n\x05\x63lose\x18\x0b \x01(\t\x12\x11\n\ttime_zone\x18\x0c \x01(\t\x12\x10\n\x08lot_size\x18\r \x01(\x03\x12\x13\n\x0bpoint_value\x18\x0e \x01(\x01\x12+\n\x05price\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x06volume\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x1f\n\x04time\x18\x11 \x01(\x0b\x32\x11.google.type.Date\x12\x0f\n\x07sources\x18\x12 \x01(\x05\x12S\n\x07mapping\x18\x13 \x03(\x0b\x32\x42.systemathics.apis.services.static_data.v1.IndexEntry.MappingEntry\x12\x11\n\tbloomberg\x18\x14 \x01(\t\x12\x0f\n\x07reuters\x18\x15 \x01(\t\x12\x13\n\x0bmorningstar\x18\x16 \x01(\t\x12\x0c\n\x04\x66igi\x18\x17 \x01(\t\x12\r\n\x05\x66igic\x18\x18 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x19 \x01(\t\x1a.\n\x0cMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\'\n\x08TickSize\x12\r\n\x05price\x18\x01 \x01(\x01\x12\x0c\n\x04tick\x18\x02 \x01(\x01*\x93\x01\n\tAssetType\x12\x1a\n\x16\x41SSET_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x41SSET_TYPE_ALL\x10\x01\x12\x15\n\x11\x41SSET_TYPE_EQUITY\x10\x02\x12\x15\n\x11\x41SSET_TYPE_FUTURE\x10\x03\x12\x12\n\x0e\x41SSET_TYPE_ETF\x10\x04\x12\x14\n\x10\x41SSET_TYPE_INDEX\x10\x05\x32\x9f\x01\n\x11StaticDataService\x12\x89\x01\n\nStaticData\x12<.systemathics.apis.services.static_data.v1.StaticDataRequest\x1a=.systemathics.apis.services.static_data.v1.StaticDataResponseb\x06proto3')

_ASSETTYPE = DESCRIPTOR.enum_types_by_name['AssetType']
AssetType = enum_type_wrapper.EnumTypeWrapper(_ASSETTYPE)
ASSET_TYPE_UNSPECIFIED = 0
ASSET_TYPE_ALL = 1
ASSET_TYPE_EQUITY = 2
ASSET_TYPE_FUTURE = 3
ASSET_TYPE_ETF = 4
ASSET_TYPE_INDEX = 5


_STATICDATAREQUEST = DESCRIPTOR.message_types_by_name['StaticDataRequest']
_STATICDATARESPONSE = DESCRIPTOR.message_types_by_name['StaticDataResponse']
_EQUITYENTRY = DESCRIPTOR.message_types_by_name['EquityEntry']
_EQUITYENTRY_MAPPINGENTRY = _EQUITYENTRY.nested_types_by_name['MappingEntry']
_EQUITYENTRY_SECTORSENTRY = _EQUITYENTRY.nested_types_by_name['SectorsEntry']
_ETFENTRY = DESCRIPTOR.message_types_by_name['EtfEntry']
_ETFENTRY_MAPPINGENTRY = _ETFENTRY.nested_types_by_name['MappingEntry']
_ETFENTRY_SECTORSENTRY = _ETFENTRY.nested_types_by_name['SectorsEntry']
_FUTUREENTRY = DESCRIPTOR.message_types_by_name['FutureEntry']
_FUTUREENTRY_MAPPINGENTRY = _FUTUREENTRY.nested_types_by_name['MappingEntry']
_FUTUREENTRY_CATEGORYENTRY = _FUTUREENTRY.nested_types_by_name['CategoryEntry']
_INDEXENTRY = DESCRIPTOR.message_types_by_name['IndexEntry']
_INDEXENTRY_MAPPINGENTRY = _INDEXENTRY.nested_types_by_name['MappingEntry']
_TICKSIZE = DESCRIPTOR.message_types_by_name['TickSize']
StaticDataRequest = _reflection.GeneratedProtocolMessageType('StaticDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATICDATAREQUEST,
  '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.StaticDataRequest)
  })
_sym_db.RegisterMessage(StaticDataRequest)

StaticDataResponse = _reflection.GeneratedProtocolMessageType('StaticDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATICDATARESPONSE,
  '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.StaticDataResponse)
  })
_sym_db.RegisterMessage(StaticDataResponse)

EquityEntry = _reflection.GeneratedProtocolMessageType('EquityEntry', (_message.Message,), {

  'MappingEntry' : _reflection.GeneratedProtocolMessageType('MappingEntry', (_message.Message,), {
    'DESCRIPTOR' : _EQUITYENTRY_MAPPINGENTRY,
    '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
    # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.EquityEntry.MappingEntry)
    })
  ,

  'SectorsEntry' : _reflection.GeneratedProtocolMessageType('SectorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EQUITYENTRY_SECTORSENTRY,
    '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
    # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.EquityEntry.SectorsEntry)
    })
  ,
  'DESCRIPTOR' : _EQUITYENTRY,
  '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.EquityEntry)
  })
_sym_db.RegisterMessage(EquityEntry)
_sym_db.RegisterMessage(EquityEntry.MappingEntry)
_sym_db.RegisterMessage(EquityEntry.SectorsEntry)

EtfEntry = _reflection.GeneratedProtocolMessageType('EtfEntry', (_message.Message,), {

  'MappingEntry' : _reflection.GeneratedProtocolMessageType('MappingEntry', (_message.Message,), {
    'DESCRIPTOR' : _ETFENTRY_MAPPINGENTRY,
    '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
    # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.EtfEntry.MappingEntry)
    })
  ,

  'SectorsEntry' : _reflection.GeneratedProtocolMessageType('SectorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ETFENTRY_SECTORSENTRY,
    '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
    # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.EtfEntry.SectorsEntry)
    })
  ,
  'DESCRIPTOR' : _ETFENTRY,
  '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.EtfEntry)
  })
_sym_db.RegisterMessage(EtfEntry)
_sym_db.RegisterMessage(EtfEntry.MappingEntry)
_sym_db.RegisterMessage(EtfEntry.SectorsEntry)

FutureEntry = _reflection.GeneratedProtocolMessageType('FutureEntry', (_message.Message,), {

  'MappingEntry' : _reflection.GeneratedProtocolMessageType('MappingEntry', (_message.Message,), {
    'DESCRIPTOR' : _FUTUREENTRY_MAPPINGENTRY,
    '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
    # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.FutureEntry.MappingEntry)
    })
  ,

  'CategoryEntry' : _reflection.GeneratedProtocolMessageType('CategoryEntry', (_message.Message,), {
    'DESCRIPTOR' : _FUTUREENTRY_CATEGORYENTRY,
    '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
    # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.FutureEntry.CategoryEntry)
    })
  ,
  'DESCRIPTOR' : _FUTUREENTRY,
  '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.FutureEntry)
  })
_sym_db.RegisterMessage(FutureEntry)
_sym_db.RegisterMessage(FutureEntry.MappingEntry)
_sym_db.RegisterMessage(FutureEntry.CategoryEntry)

IndexEntry = _reflection.GeneratedProtocolMessageType('IndexEntry', (_message.Message,), {

  'MappingEntry' : _reflection.GeneratedProtocolMessageType('MappingEntry', (_message.Message,), {
    'DESCRIPTOR' : _INDEXENTRY_MAPPINGENTRY,
    '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
    # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.IndexEntry.MappingEntry)
    })
  ,
  'DESCRIPTOR' : _INDEXENTRY,
  '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.IndexEntry)
  })
_sym_db.RegisterMessage(IndexEntry)
_sym_db.RegisterMessage(IndexEntry.MappingEntry)

TickSize = _reflection.GeneratedProtocolMessageType('TickSize', (_message.Message,), {
  'DESCRIPTOR' : _TICKSIZE,
  '__module__' : 'systemathics.apis.services.static_data.v1.static_data_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.static_data.v1.TickSize)
  })
_sym_db.RegisterMessage(TickSize)

_STATICDATASERVICE = DESCRIPTOR.services_by_name['StaticDataService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EQUITYENTRY_MAPPINGENTRY._options = None
  _EQUITYENTRY_MAPPINGENTRY._serialized_options = b'8\001'
  _EQUITYENTRY_SECTORSENTRY._options = None
  _EQUITYENTRY_SECTORSENTRY._serialized_options = b'8\001'
  _ETFENTRY_MAPPINGENTRY._options = None
  _ETFENTRY_MAPPINGENTRY._serialized_options = b'8\001'
  _ETFENTRY_SECTORSENTRY._options = None
  _ETFENTRY_SECTORSENTRY._serialized_options = b'8\001'
  _FUTUREENTRY_MAPPINGENTRY._options = None
  _FUTUREENTRY_MAPPINGENTRY._serialized_options = b'8\001'
  _FUTUREENTRY_CATEGORYENTRY._options = None
  _FUTUREENTRY_CATEGORYENTRY._serialized_options = b'8\001'
  _INDEXENTRY_MAPPINGENTRY._options = None
  _INDEXENTRY_MAPPINGENTRY._serialized_options = b'8\001'
  _ASSETTYPE._serialized_start=4936
  _ASSETTYPE._serialized_end=5083
  _STATICDATAREQUEST._serialized_start=214
  _STATICDATAREQUEST._serialized_end=785
  _STATICDATARESPONSE._serialized_start=788
  _STATICDATARESPONSE._serialized_end=1094
  _EQUITYENTRY._serialized_start=1097
  _EQUITYENTRY._serialized_end=2140
  _EQUITYENTRY_MAPPINGENTRY._serialized_start=2046
  _EQUITYENTRY_MAPPINGENTRY._serialized_end=2092
  _EQUITYENTRY_SECTORSENTRY._serialized_start=2094
  _EQUITYENTRY_SECTORSENTRY._serialized_end=2140
  _ETFENTRY._serialized_start=2143
  _ETFENTRY._serialized_end=3177
  _ETFENTRY_MAPPINGENTRY._serialized_start=2046
  _ETFENTRY_MAPPINGENTRY._serialized_end=2092
  _ETFENTRY_SECTORSENTRY._serialized_start=2094
  _ETFENTRY_SECTORSENTRY._serialized_end=2140
  _FUTUREENTRY._serialized_start=3180
  _FUTUREENTRY._serialized_end=4153
  _FUTUREENTRY_MAPPINGENTRY._serialized_start=2046
  _FUTUREENTRY_MAPPINGENTRY._serialized_end=2092
  _FUTUREENTRY_CATEGORYENTRY._serialized_start=4106
  _FUTUREENTRY_CATEGORYENTRY._serialized_end=4153
  _INDEXENTRY._serialized_start=4156
  _INDEXENTRY._serialized_end=4892
  _INDEXENTRY_MAPPINGENTRY._serialized_start=2046
  _INDEXENTRY_MAPPINGENTRY._serialized_end=2092
  _TICKSIZE._serialized_start=4894
  _TICKSIZE._serialized_end=4933
  _STATICDATASERVICE._serialized_start=5086
  _STATICDATASERVICE._serialized_end=5245
# @@protoc_insertion_point(module_scope)
