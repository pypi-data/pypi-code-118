# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/meeting/v1/meeting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_team_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.services.common.v1 import common_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?github.com/metaprov/modelaapi/services/meeting/v1/meeting.proto\x12\x31github.com.metaprov.modelaapi.services.meeting.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/team/v1alpha1/generated.proto\x1a=github.com/metaprov/modelaapi/services/common/v1/common.proto\"\xf4\x01\n\x13ListMeetingsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x62\n\x06labels\x18\x02 \x03(\x0b\x32R.github.com.metaprov.modelaapi.services.meeting.v1.ListMeetingsRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\x14ListMeetingsResponse\x12S\n\x08meetings\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.MeetingList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x11\n\x0fMeetingResponse\"x\n\x14\x43reateMeetingRequest\x12N\n\x07meeting\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.Meeting\x12\x10\n\x08password\x18\x02 \x01(\t\"\x17\n\x15\x43reateMeetingResponse\"\x96\x01\n\x14UpdateMeetingRequest\x12N\n\x07meeting\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.Meeting\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x17\n\x15UpdateMeetingResponse\"4\n\x11GetMeetingRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"r\n\x12GetMeetingResponse\x12N\n\x07meeting\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.Meeting\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"7\n\x14\x44\x65leteMeetingRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x17\n\x15\x44\x65leteMeetingResponse2\x98\x08\n\x0eMeetingService\x12\xc1\x01\n\x0cListMeetings\x12\x46.github.com.metaprov.modelaapi.services.meeting.v1.ListMeetingsRequest\x1aG.github.com.metaprov.modelaapi.services.meeting.v1.ListMeetingsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/meetings/{namespace}\x12\xbb\x01\n\rCreateMeeting\x12G.github.com.metaprov.modelaapi.services.meeting.v1.CreateMeetingRequest\x1aH.github.com.metaprov.modelaapi.services.meeting.v1.CreateMeetingResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/meetings:\x01*\x12\xc2\x01\n\nGetMeeting\x12\x44.github.com.metaprov.modelaapi.services.meeting.v1.GetMeetingRequest\x1a\x45.github.com.metaprov.modelaapi.services.meeting.v1.GetMeetingResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/meetings/{namespace}/{name}\x12\xf0\x01\n\rUpdateMeeting\x12G.github.com.metaprov.modelaapi.services.meeting.v1.UpdateMeetingRequest\x1aH.github.com.metaprov.modelaapi.services.meeting.v1.UpdateMeetingResponse\"L\x82\xd3\xe4\x93\x02\x46\x1a\x41/v1/meetings/{meeting.metadata.namespace}/{meeting.metadata.name}:\x01*\x12\xcb\x01\n\rDeleteMeeting\x12G.github.com.metaprov.modelaapi.services.meeting.v1.DeleteMeetingRequest\x1aH.github.com.metaprov.modelaapi.services.meeting.v1.DeleteMeetingResponse\"\'\x82\xd3\xe4\x93\x02!*\x1f/v1/meetings/{namespace}/{name}B3Z1github.com/metaprov/modelaapi/services/meeting/v1b\x06proto3')



_LISTMEETINGSREQUEST = DESCRIPTOR.message_types_by_name['ListMeetingsRequest']
_LISTMEETINGSREQUEST_LABELSENTRY = _LISTMEETINGSREQUEST.nested_types_by_name['LabelsEntry']
_LISTMEETINGSRESPONSE = DESCRIPTOR.message_types_by_name['ListMeetingsResponse']
_MEETINGRESPONSE = DESCRIPTOR.message_types_by_name['MeetingResponse']
_CREATEMEETINGREQUEST = DESCRIPTOR.message_types_by_name['CreateMeetingRequest']
_CREATEMEETINGRESPONSE = DESCRIPTOR.message_types_by_name['CreateMeetingResponse']
_UPDATEMEETINGREQUEST = DESCRIPTOR.message_types_by_name['UpdateMeetingRequest']
_UPDATEMEETINGRESPONSE = DESCRIPTOR.message_types_by_name['UpdateMeetingResponse']
_GETMEETINGREQUEST = DESCRIPTOR.message_types_by_name['GetMeetingRequest']
_GETMEETINGRESPONSE = DESCRIPTOR.message_types_by_name['GetMeetingResponse']
_DELETEMEETINGREQUEST = DESCRIPTOR.message_types_by_name['DeleteMeetingRequest']
_DELETEMEETINGRESPONSE = DESCRIPTOR.message_types_by_name['DeleteMeetingResponse']
ListMeetingsRequest = _reflection.GeneratedProtocolMessageType('ListMeetingsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTMEETINGSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.ListMeetingsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTMEETINGSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.ListMeetingsRequest)
  })
_sym_db.RegisterMessage(ListMeetingsRequest)
_sym_db.RegisterMessage(ListMeetingsRequest.LabelsEntry)

ListMeetingsResponse = _reflection.GeneratedProtocolMessageType('ListMeetingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMEETINGSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.ListMeetingsResponse)
  })
_sym_db.RegisterMessage(ListMeetingsResponse)

MeetingResponse = _reflection.GeneratedProtocolMessageType('MeetingResponse', (_message.Message,), {
  'DESCRIPTOR' : _MEETINGRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.MeetingResponse)
  })
_sym_db.RegisterMessage(MeetingResponse)

CreateMeetingRequest = _reflection.GeneratedProtocolMessageType('CreateMeetingRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMEETINGREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.CreateMeetingRequest)
  })
_sym_db.RegisterMessage(CreateMeetingRequest)

CreateMeetingResponse = _reflection.GeneratedProtocolMessageType('CreateMeetingResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMEETINGRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.CreateMeetingResponse)
  })
_sym_db.RegisterMessage(CreateMeetingResponse)

UpdateMeetingRequest = _reflection.GeneratedProtocolMessageType('UpdateMeetingRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEETINGREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.UpdateMeetingRequest)
  })
_sym_db.RegisterMessage(UpdateMeetingRequest)

UpdateMeetingResponse = _reflection.GeneratedProtocolMessageType('UpdateMeetingResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEETINGRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.UpdateMeetingResponse)
  })
_sym_db.RegisterMessage(UpdateMeetingResponse)

GetMeetingRequest = _reflection.GeneratedProtocolMessageType('GetMeetingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMEETINGREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.GetMeetingRequest)
  })
_sym_db.RegisterMessage(GetMeetingRequest)

GetMeetingResponse = _reflection.GeneratedProtocolMessageType('GetMeetingResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMEETINGRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.GetMeetingResponse)
  })
_sym_db.RegisterMessage(GetMeetingResponse)

DeleteMeetingRequest = _reflection.GeneratedProtocolMessageType('DeleteMeetingRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMEETINGREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.DeleteMeetingRequest)
  })
_sym_db.RegisterMessage(DeleteMeetingRequest)

DeleteMeetingResponse = _reflection.GeneratedProtocolMessageType('DeleteMeetingResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMEETINGRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.meeting.v1.meeting_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.meeting.v1.DeleteMeetingResponse)
  })
_sym_db.RegisterMessage(DeleteMeetingResponse)

_MEETINGSERVICE = DESCRIPTOR.services_by_name['MeetingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/metaprov/modelaapi/services/meeting/v1'
  _LISTMEETINGSREQUEST_LABELSENTRY._options = None
  _LISTMEETINGSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _MEETINGSERVICE.methods_by_name['ListMeetings']._options = None
  _MEETINGSERVICE.methods_by_name['ListMeetings']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/meetings/{namespace}'
  _MEETINGSERVICE.methods_by_name['CreateMeeting']._options = None
  _MEETINGSERVICE.methods_by_name['CreateMeeting']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/meetings:\001*'
  _MEETINGSERVICE.methods_by_name['GetMeeting']._options = None
  _MEETINGSERVICE.methods_by_name['GetMeeting']._serialized_options = b'\202\323\344\223\002!\022\037/v1/meetings/{namespace}/{name}'
  _MEETINGSERVICE.methods_by_name['UpdateMeeting']._options = None
  _MEETINGSERVICE.methods_by_name['UpdateMeeting']._serialized_options = b'\202\323\344\223\002F\032A/v1/meetings/{meeting.metadata.namespace}/{meeting.metadata.name}:\001*'
  _MEETINGSERVICE.methods_by_name['DeleteMeeting']._options = None
  _MEETINGSERVICE.methods_by_name['DeleteMeeting']._serialized_options = b'\202\323\344\223\002!*\037/v1/meetings/{namespace}/{name}'
  _LISTMEETINGSREQUEST._serialized_start=316
  _LISTMEETINGSREQUEST._serialized_end=560
  _LISTMEETINGSREQUEST_LABELSENTRY._serialized_start=515
  _LISTMEETINGSREQUEST_LABELSENTRY._serialized_end=560
  _LISTMEETINGSRESPONSE._serialized_start=563
  _LISTMEETINGSRESPONSE._serialized_end=695
  _MEETINGRESPONSE._serialized_start=697
  _MEETINGRESPONSE._serialized_end=714
  _CREATEMEETINGREQUEST._serialized_start=716
  _CREATEMEETINGREQUEST._serialized_end=836
  _CREATEMEETINGRESPONSE._serialized_start=838
  _CREATEMEETINGRESPONSE._serialized_end=861
  _UPDATEMEETINGREQUEST._serialized_start=864
  _UPDATEMEETINGREQUEST._serialized_end=1014
  _UPDATEMEETINGRESPONSE._serialized_start=1016
  _UPDATEMEETINGRESPONSE._serialized_end=1039
  _GETMEETINGREQUEST._serialized_start=1041
  _GETMEETINGREQUEST._serialized_end=1093
  _GETMEETINGRESPONSE._serialized_start=1095
  _GETMEETINGRESPONSE._serialized_end=1209
  _DELETEMEETINGREQUEST._serialized_start=1211
  _DELETEMEETINGREQUEST._serialized_end=1266
  _DELETEMEETINGRESPONSE._serialized_start=1268
  _DELETEMEETINGRESPONSE._serialized_end=1291
  _MEETINGSERVICE._serialized_start=1294
  _MEETINGSERVICE._serialized_end=2342
# @@protoc_insertion_point(module_scope)
