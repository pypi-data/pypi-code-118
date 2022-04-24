# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/common/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cservices/common/common.proto\x12\rsocial.common\"\x12\n\x04Pong\x12\n\n\x02ts\x18\x01 \x01(\x03\";\n\x0b\x46indRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\"\x07\n\x05\x45mpty\"\xcc\x01\n\x05Media\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x10\n\x08\x64uration\x18\x05 \x01(\x05\x12\x31\n\x0cmention_list\x18\x06 \x03(\x0b\x32\x1b.social.common.MediaMention\x12\x10\n\x08\x66ilename\x18\x07 \x01(\t\x12\x11\n\tthumbnail\x18\x08 \x01(\t\x12\x11\n\tthumb_url\x18\t \x01(\t\x12\x0c\n\x04link\x18\n \x01(\t\"6\n\x0cMediaMention\x12\x10\n\x08username\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\")\n\x13UploadMediaResponse\x12\x12\n\nupload_url\x18\x01 \x01(\t\"4\n\x12UploadMediaRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"+\n\nPagination\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"\x1d\n\x0c\x42ooleanValue\x12\r\n\x05value\x18\x01 \x01(\x08\"\x1b\n\nInt64Value\x12\r\n\x05value\x18\x01 \x01(\x03\"%\n\x08\x43\x61tegory\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\"9\n\x0f\x43\x61tListResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.social.common.Category\"3\n\x08Location\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03lat\x18\x02 \x01(\x01\x12\x0c\n\x04long\x18\x03 \x01(\x01\"Q\n\rPublishStatus\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .social.common.PublishStatusEnum\x12\x0e\n\x06reason\x18\x02 \x01(\t\"D\n\x14PublishStatusRequest\x12,\n\x06status\x18\x01 \x01(\x0b\x32\x1c.social.common.PublishStatus\"0\n\x04\x44\x61te\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05*<\n\x11PublishStatusEnum\x12\x0b\n\x07PENDING\x10\x00\x12\x0c\n\x08\x41PPROVED\x10\x01\x12\x0c\n\x08REJECTED\x10\x02\x62\x06proto3')

_PUBLISHSTATUSENUM = DESCRIPTOR.enum_types_by_name['PublishStatusEnum']
PublishStatusEnum = enum_type_wrapper.EnumTypeWrapper(_PUBLISHSTATUSENUM)
PENDING = 0
APPROVED = 1
REJECTED = 2


_PONG = DESCRIPTOR.message_types_by_name['Pong']
_FINDREQUEST = DESCRIPTOR.message_types_by_name['FindRequest']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_MEDIA = DESCRIPTOR.message_types_by_name['Media']
_MEDIAMENTION = DESCRIPTOR.message_types_by_name['MediaMention']
_UPLOADMEDIARESPONSE = DESCRIPTOR.message_types_by_name['UploadMediaResponse']
_UPLOADMEDIAREQUEST = DESCRIPTOR.message_types_by_name['UploadMediaRequest']
_PAGINATION = DESCRIPTOR.message_types_by_name['Pagination']
_BOOLEANVALUE = DESCRIPTOR.message_types_by_name['BooleanValue']
_INT64VALUE = DESCRIPTOR.message_types_by_name['Int64Value']
_CATEGORY = DESCRIPTOR.message_types_by_name['Category']
_CATLISTRESPONSE = DESCRIPTOR.message_types_by_name['CatListResponse']
_LOCATION = DESCRIPTOR.message_types_by_name['Location']
_PUBLISHSTATUS = DESCRIPTOR.message_types_by_name['PublishStatus']
_PUBLISHSTATUSREQUEST = DESCRIPTOR.message_types_by_name['PublishStatusRequest']
_DATE = DESCRIPTOR.message_types_by_name['Date']
Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Pong)
  })
_sym_db.RegisterMessage(Pong)

FindRequest = _reflection.GeneratedProtocolMessageType('FindRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDREQUEST,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.FindRequest)
  })
_sym_db.RegisterMessage(FindRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Empty)
  })
_sym_db.RegisterMessage(Empty)

Media = _reflection.GeneratedProtocolMessageType('Media', (_message.Message,), {
  'DESCRIPTOR' : _MEDIA,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Media)
  })
_sym_db.RegisterMessage(Media)

MediaMention = _reflection.GeneratedProtocolMessageType('MediaMention', (_message.Message,), {
  'DESCRIPTOR' : _MEDIAMENTION,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.MediaMention)
  })
_sym_db.RegisterMessage(MediaMention)

UploadMediaResponse = _reflection.GeneratedProtocolMessageType('UploadMediaResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMEDIARESPONSE,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.UploadMediaResponse)
  })
_sym_db.RegisterMessage(UploadMediaResponse)

UploadMediaRequest = _reflection.GeneratedProtocolMessageType('UploadMediaRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMEDIAREQUEST,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.UploadMediaRequest)
  })
_sym_db.RegisterMessage(UploadMediaRequest)

Pagination = _reflection.GeneratedProtocolMessageType('Pagination', (_message.Message,), {
  'DESCRIPTOR' : _PAGINATION,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Pagination)
  })
_sym_db.RegisterMessage(Pagination)

BooleanValue = _reflection.GeneratedProtocolMessageType('BooleanValue', (_message.Message,), {
  'DESCRIPTOR' : _BOOLEANVALUE,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.BooleanValue)
  })
_sym_db.RegisterMessage(BooleanValue)

Int64Value = _reflection.GeneratedProtocolMessageType('Int64Value', (_message.Message,), {
  'DESCRIPTOR' : _INT64VALUE,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Int64Value)
  })
_sym_db.RegisterMessage(Int64Value)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Category)
  })
_sym_db.RegisterMessage(Category)

CatListResponse = _reflection.GeneratedProtocolMessageType('CatListResponse', (_message.Message,), {
  'DESCRIPTOR' : _CATLISTRESPONSE,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.CatListResponse)
  })
_sym_db.RegisterMessage(CatListResponse)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Location)
  })
_sym_db.RegisterMessage(Location)

PublishStatus = _reflection.GeneratedProtocolMessageType('PublishStatus', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHSTATUS,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.PublishStatus)
  })
_sym_db.RegisterMessage(PublishStatus)

PublishStatusRequest = _reflection.GeneratedProtocolMessageType('PublishStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHSTATUSREQUEST,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.PublishStatusRequest)
  })
_sym_db.RegisterMessage(PublishStatusRequest)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'services.common.common_pb2'
  # @@protoc_insertion_point(class_scope:social.common.Date)
  })
_sym_db.RegisterMessage(Date)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PUBLISHSTATUSENUM._serialized_start=956
  _PUBLISHSTATUSENUM._serialized_end=1016
  _PONG._serialized_start=47
  _PONG._serialized_end=65
  _FINDREQUEST._serialized_start=67
  _FINDREQUEST._serialized_end=126
  _EMPTY._serialized_start=128
  _EMPTY._serialized_end=135
  _MEDIA._serialized_start=138
  _MEDIA._serialized_end=342
  _MEDIAMENTION._serialized_start=344
  _MEDIAMENTION._serialized_end=398
  _UPLOADMEDIARESPONSE._serialized_start=400
  _UPLOADMEDIARESPONSE._serialized_end=441
  _UPLOADMEDIAREQUEST._serialized_start=443
  _UPLOADMEDIAREQUEST._serialized_end=495
  _PAGINATION._serialized_start=497
  _PAGINATION._serialized_end=540
  _BOOLEANVALUE._serialized_start=542
  _BOOLEANVALUE._serialized_end=571
  _INT64VALUE._serialized_start=573
  _INT64VALUE._serialized_end=600
  _CATEGORY._serialized_start=602
  _CATEGORY._serialized_end=639
  _CATLISTRESPONSE._serialized_start=641
  _CATLISTRESPONSE._serialized_end=698
  _LOCATION._serialized_start=700
  _LOCATION._serialized_end=751
  _PUBLISHSTATUS._serialized_start=753
  _PUBLISHSTATUS._serialized_end=834
  _PUBLISHSTATUSREQUEST._serialized_start=836
  _PUBLISHSTATUSREQUEST._serialized_end=904
  _DATE._serialized_start=906
  _DATE._serialized_end=954
# @@protoc_insertion_point(module_scope)
