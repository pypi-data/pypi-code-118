# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/history/history.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.api.services.common import common_pb2 as services_dot_common_dot_common__pb2
from common.api.services.account import account_pb2 as services_dot_account_dot_account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservices/history/history.proto\x12\x0esocial.history\x1a\x1cservices/common/common.proto\x1a\x1eservices/account/account.proto\"\xb1\x01\n\x03\x41\x63t\x12\n\n\x02id\x18\x01 \x01(\t\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.social.history.ActTypes\x12\x0b\n\x03obj\x18\x03 \x01(\t\x12\r\n\x05obj_o\x18\x04 \x01(\t\x12&\n\x05\x61\x63tor\x18\x05 \x01(\x0b\x32\x17.social.account.Account\x12&\n\x04verb\x18\x06 \x01(\x0e\x32\x18.social.history.ActVerbs\x12\n\n\x02\x61t\x18\x07 \x01(\x03\"5\n\x14GetActivitiesRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"5\n\x0f\x41\x63tListResponse\x12\"\n\x05items\x18\x01 \x03(\x0b\x32\x13.social.history.Act*I\n\x08\x41\x63tTypes\x12\x0b\n\x07\x41\x43\x43OUNT\x10\x00\x12\x08\n\x04POST\x10\x01\x12\t\n\x05STORY\x10\x02\x12\x0e\n\nDISCUSSION\x10\x03\x12\x0b\n\x07HASHTAG\x10\x04*\xfa\x01\n\x08\x41\x63tVerbs\x12\x08\n\x04LIKE\x10\x00\x12\n\n\x06UNLIKE\x10\x01\x12\n\n\x06\x46OLLOW\x10\x02\x12\x0c\n\x08UNFOLLOW\x10\x03\x12\x12\n\x0e\x46OLLOW_REQUEST\x10\x04\x12\x07\n\x03TAG\x10\x05\x12\x0b\n\x07MENTION\x10\x06\x12\x0b\n\x07\x43OMMENT\x10\x07\x12\t\n\x05LOGIN\x10\x62\x12\n\n\x06LOGOUT\x10\x63\x12\t\n\x05\x42LOCK\x10\x64\x12\x0e\n\nCHANGE_BIO\x10\x65\x12\x17\n\x13\x43HANGE_DISPLAY_NAME\x10\x66\x12\x13\n\x0f\x43HANGE_USERNAME\x10g\x12\x13\n\x0fPRIVATE_ACCOUNT\x10n\x12\x12\n\x0ePUBLIC_ACCOUNT\x10o2\xcd\x01\n\x0eHistoryService\x12\x31\n\x04Ping\x12\x14.social.common.Empty\x1a\x13.social.common.Pong\x12V\n\rGetActivities\x12$.social.history.GetActivitiesRequest\x1a\x1f.social.history.ActListResponse\x12\x30\n\x03Log\x12\x13.social.history.Act\x1a\x14.social.common.Emptyb\x06proto3')

_ACTTYPES = DESCRIPTOR.enum_types_by_name['ActTypes']
ActTypes = enum_type_wrapper.EnumTypeWrapper(_ACTTYPES)
_ACTVERBS = DESCRIPTOR.enum_types_by_name['ActVerbs']
ActVerbs = enum_type_wrapper.EnumTypeWrapper(_ACTVERBS)
ACCOUNT = 0
POST = 1
STORY = 2
DISCUSSION = 3
HASHTAG = 4
LIKE = 0
UNLIKE = 1
FOLLOW = 2
UNFOLLOW = 3
FOLLOW_REQUEST = 4
TAG = 5
MENTION = 6
COMMENT = 7
LOGIN = 98
LOGOUT = 99
BLOCK = 100
CHANGE_BIO = 101
CHANGE_DISPLAY_NAME = 102
CHANGE_USERNAME = 103
PRIVATE_ACCOUNT = 110
PUBLIC_ACCOUNT = 111


_ACT = DESCRIPTOR.message_types_by_name['Act']
_GETACTIVITIESREQUEST = DESCRIPTOR.message_types_by_name['GetActivitiesRequest']
_ACTLISTRESPONSE = DESCRIPTOR.message_types_by_name['ActListResponse']
Act = _reflection.GeneratedProtocolMessageType('Act', (_message.Message,), {
  'DESCRIPTOR' : _ACT,
  '__module__' : 'services.history.history_pb2'
  # @@protoc_insertion_point(class_scope:social.history.Act)
  })
_sym_db.RegisterMessage(Act)

GetActivitiesRequest = _reflection.GeneratedProtocolMessageType('GetActivitiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIVITIESREQUEST,
  '__module__' : 'services.history.history_pb2'
  # @@protoc_insertion_point(class_scope:social.history.GetActivitiesRequest)
  })
_sym_db.RegisterMessage(GetActivitiesRequest)

ActListResponse = _reflection.GeneratedProtocolMessageType('ActListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTLISTRESPONSE,
  '__module__' : 'services.history.history_pb2'
  # @@protoc_insertion_point(class_scope:social.history.ActListResponse)
  })
_sym_db.RegisterMessage(ActListResponse)

_HISTORYSERVICE = DESCRIPTOR.services_by_name['HistoryService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACTTYPES._serialized_start=402
  _ACTTYPES._serialized_end=475
  _ACTVERBS._serialized_start=478
  _ACTVERBS._serialized_end=728
  _ACT._serialized_start=113
  _ACT._serialized_end=290
  _GETACTIVITIESREQUEST._serialized_start=292
  _GETACTIVITIESREQUEST._serialized_end=345
  _ACTLISTRESPONSE._serialized_start=347
  _ACTLISTRESPONSE._serialized_end=400
  _HISTORYSERVICE._serialized_start=731
  _HISTORYSERVICE._serialized_end=936
# @@protoc_insertion_point(module_scope)
