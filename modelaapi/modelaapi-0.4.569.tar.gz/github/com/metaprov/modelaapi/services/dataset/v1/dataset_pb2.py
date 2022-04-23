# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/dataset/v1/dataset.proto
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
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.services.common.v1 import common_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?github.com/metaprov/modelaapi/services/dataset/v1/dataset.proto\x12\x31github.com.metaprov.modelaapi.services.dataset.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/data/v1alpha1/generated.proto\x1a=github.com/metaprov/modelaapi/services/common/v1/common.proto\"\xf4\x01\n\x13ListDatasetsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x62\n\x06labels\x18\x02 \x03(\x0b\x32R.github.com.metaprov.modelaapi.services.dataset.v1.ListDatasetsRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\x14ListDatasetsResponse\x12S\n\x08\x64\x61tasets\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DatasetList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc5\x01\n\x11GetDatasetRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12`\n\x06labels\x18\x03 \x03(\x0b\x32P.github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"r\n\x12GetDatasetResponse\x12N\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"f\n\x14\x43reateDatasetRequest\x12N\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\"\x17\n\x15\x43reateDatasetResponse\"\x96\x01\n\x14UpdateDatasetRequest\x12N\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x17\n\x15UpdateDatasetResponse\"7\n\x14\x44\x65leteDatasetRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x17\n\x15\x44\x65leteDatasetResponse\"Q\n\x12UploadChunkRequest\x12\r\n\x05\x66name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\r\n\x05index\x18\x03 \x01(\x05\x12\x0c\n\x04last\x18\x04 \x01(\x08\"0\n\x13UploadChunkResponse\x12\r\n\x05\x66name\x18\x01 \x01(\t\x12\n\n\x02ok\x18\x02 \x01(\x08\"\x8e\x01\n\x1b\x43reateDatasetProfileRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12N\n\x07\x64\x61taset\x18\x03 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\"~\n\x1c\x43reateDatasetProfileResponse\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12Q\n\x07profile\x18\x02 \x01(\x0b\x32@.github.com.metaprov.modelaapi.services.common.v1.DatasetProfile\"\x9a\x01\n\x1a\x43reateColumnProfileRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x63ol\x18\x03 \x01(\t\x12N\n\x07\x64\x61taset\x18\x04 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\"q\n\x1b\x43reateColumnProfileResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x44\n\x04plot\x18\x02 \x01(\x0b\x32\x36.github.com.metaprov.modelaapi.services.common.v1.Plot\"H\n\x18GetDatasetProfileRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\"\x8f\x01\n\x19GetDatasetProfileResponse\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12Q\n\x07profile\x18\x03 \x01(\x0b\x32@.github.com.metaprov.modelaapi.services.common.v1.DatasetProfile\":\n\x16\x43ompareDatasetsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\"\x8f\x01\n\x17\x43ompareDatasetsResponse\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\x12R\n\x08profiles\x18\x03 \x03(\x0b\x32@.github.com.metaprov.modelaapi.services.common.v1.DatasetProfile\":\n\x16GenerateDatasetRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\"\x8f\x01\n\x17GenerateDatasetResponse\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\x12R\n\x08profiles\x18\x03 \x03(\x0b\x32@.github.com.metaprov.modelaapi.services.common.v1.DatasetProfile\":\n\x16ValidateDatasetRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\"\x8f\x01\n\x17ValidateDatasetResponse\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05names\x18\x02 \x03(\t\x12R\n\x08profiles\x18\x03 \x03(\x0b\x32@.github.com.metaprov.modelaapi.services.common.v1.DatasetProfile\"9\n\x16\x44ownloadDatasetRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"&\n\x17\x44ownloadDatasetResponse\x12\x0b\n\x03raw\x18\x01 \x01(\x0c\"J\n\x13GetDatabasesRequest\x12\x1b\n\x13\x63onnectionNamespace\x18\x01 \x01(\t\x12\x16\n\x0e\x63onnectionName\x18\x02 \x01(\t\")\n\x14GetDatabasesResponse\x12\x11\n\tdatabases\x18\x01 \x03(\t\"]\n\x10GetTablesRequest\x12\x1b\n\x13\x63onnectionNamespace\x18\x01 \x01(\t\x12\x16\n\x0e\x63onnectionName\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x61tabaseName\x18\x03 \x01(\t\"#\n\x11GetTablesResponse\x12\x0e\n\x06tables\x18\x01 \x03(\t\"k\n\x11\x45xecuteSqlRequest\x12\x1b\n\x13\x63onnectionNamespace\x18\x01 \x01(\t\x12\x16\n\x0e\x63onnectionName\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x61tabaseName\x18\x03 \x01(\t\x12\x0b\n\x03sql\x18\x04 \x01(\t\"d\n\x12\x45xecuteSqlResponse\x12N\n\ttableview\x18\x01 \x01(\x0b\x32;.github.com.metaprov.modelaapi.services.common.v1.TableView\"i\n\x0fSnapshotRequest\x12\x1b\n\x13\x63onnectionNamespace\x18\x01 \x01(\t\x12\x16\n\x0e\x63onnectionName\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x61tabaseName\x18\x03 \x01(\t\x12\x0b\n\x03sql\x18\x04 \x01(\t\"0\n\x10SnapshotResponse\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t2\xe4\x19\n\x0e\x44\x61tasetService\x12\xc1\x01\n\x0cListDatasets\x12\x46.github.com.metaprov.modelaapi.services.dataset.v1.ListDatasetsRequest\x1aG.github.com.metaprov.modelaapi.services.dataset.v1.ListDatasetsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/datasets/{namespace}\x12\xc2\x01\n\nGetDataset\x12\x44.github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetRequest\x1a\x45.github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/datasets/{namespace}/{name}\x12\xbb\x01\n\rCreateDataset\x12G.github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetRequest\x1aH.github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/datasets:\x01*\x12\xf0\x01\n\rUpdateDataset\x12G.github.com.metaprov.modelaapi.services.dataset.v1.UpdateDatasetRequest\x1aH.github.com.metaprov.modelaapi.services.dataset.v1.UpdateDatasetResponse\"L\x82\xd3\xe4\x93\x02\x46\x1a\x41/v1/datasets/{dataset.metadata.namespace}/{dataset.metadata.name}:\x01*\x12\xbf\x01\n\rDeleteDataset\x12G.github.com.metaprov.modelaapi.services.dataset.v1.DeleteDatasetRequest\x1aH.github.com.metaprov.modelaapi.services.dataset.v1.DeleteDatasetResponse\"\x1b\x82\xd3\xe4\x93\x02\x15*\x13/v1/datasets/{name}\x12\xda\x01\n\x0f\x43ompareDatasets\x12I.github.com.metaprov.modelaapi.services.dataset.v1.CompareDatasetsRequest\x1aJ.github.com.metaprov.modelaapi.services.dataset.v1.CompareDatasetsResponse\"0\x82\xd3\xe4\x93\x02*\"(/v1/datasets/{namespace}/{names}:compare\x12\xdf\x01\n\x11GetDatasetProfile\x12K.github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetProfileRequest\x1aL.github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetProfileResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/v1/datasets/{namespace}/{name}:profile\x12\xe8\x01\n\x14\x43reateDatasetProfile\x12N.github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetProfileRequest\x1aO.github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetProfileResponse\"/\x82\xd3\xe4\x93\x02)\"\'/v1/datasets/{namespace}/{name}:profile\x12\xe8\x01\n\x13\x43reateColumnProfile\x12M.github.com.metaprov.modelaapi.services.dataset.v1.CreateColumnProfileRequest\x1aN.github.com.metaprov.modelaapi.services.dataset.v1.CreateColumnProfileResponse\"2\x82\xd3\xe4\x93\x02,\"*/v1/datasets/{namespace}/{name}/columnplot\x12\xdb\x01\n\x0fGenerateDataset\x12I.github.com.metaprov.modelaapi.services.dataset.v1.GenerateDatasetRequest\x1aJ.github.com.metaprov.modelaapi.services.dataset.v1.GenerateDatasetResponse\"1\x82\xd3\xe4\x93\x02+\")/v1/datasets/{namespace}/{names}:generate\x12\xdb\x01\n\x0fValidateDataset\x12I.github.com.metaprov.modelaapi.services.dataset.v1.ValidateDatasetRequest\x1aJ.github.com.metaprov.modelaapi.services.dataset.v1.ValidateDatasetResponse\"1\x82\xd3\xe4\x93\x02+\")/v1/datasets/{namespace}/{names}:validate\x12\xda\x01\n\x0f\x44ownloadDataset\x12I.github.com.metaprov.modelaapi.services.dataset.v1.DownloadDatasetRequest\x1aJ.github.com.metaprov.modelaapi.services.dataset.v1.DownloadDatasetResponse\"0\x82\xd3\xe4\x93\x02*\"(/v1/datasets/{namespace}/{name}:download\x12\xe6\x01\n\x0cGetDatabases\x12\x46.github.com.metaprov.modelaapi.services.dataset.v1.GetDatabasesRequest\x1aG.github.com.metaprov.modelaapi.services.dataset.v1.GetDatabasesResponse\"E\x82\xd3\xe4\x93\x02?\x12=/v1/datasets/{connectionNamespace}/{connectionName}:databases\x12\xda\x01\n\tGetTables\x12\x43.github.com.metaprov.modelaapi.services.dataset.v1.GetTablesRequest\x1a\x44.github.com.metaprov.modelaapi.services.dataset.v1.GetTablesResponse\"B\x82\xd3\xe4\x93\x02<\x12:/v1/datasets/{connectionNamespace}/{connectionName}:tables\x12\xe1\x01\n\nExecuteSql\x12\x44.github.com.metaprov.modelaapi.services.dataset.v1.ExecuteSqlRequest\x1a\x45.github.com.metaprov.modelaapi.services.dataset.v1.ExecuteSqlResponse\"F\x82\xd3\xe4\x93\x02@\">/v1/datasets/{connectionNamespace}/{connectionName}:executesqlB3Z1github.com/metaprov/modelaapi/services/dataset/v1b\x06proto3')



_LISTDATASETSREQUEST = DESCRIPTOR.message_types_by_name['ListDatasetsRequest']
_LISTDATASETSREQUEST_LABELSENTRY = _LISTDATASETSREQUEST.nested_types_by_name['LabelsEntry']
_LISTDATASETSRESPONSE = DESCRIPTOR.message_types_by_name['ListDatasetsResponse']
_GETDATASETREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetRequest']
_GETDATASETREQUEST_LABELSENTRY = _GETDATASETREQUEST.nested_types_by_name['LabelsEntry']
_GETDATASETRESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetResponse']
_CREATEDATASETREQUEST = DESCRIPTOR.message_types_by_name['CreateDatasetRequest']
_CREATEDATASETRESPONSE = DESCRIPTOR.message_types_by_name['CreateDatasetResponse']
_UPDATEDATASETREQUEST = DESCRIPTOR.message_types_by_name['UpdateDatasetRequest']
_UPDATEDATASETRESPONSE = DESCRIPTOR.message_types_by_name['UpdateDatasetResponse']
_DELETEDATASETREQUEST = DESCRIPTOR.message_types_by_name['DeleteDatasetRequest']
_DELETEDATASETRESPONSE = DESCRIPTOR.message_types_by_name['DeleteDatasetResponse']
_UPLOADCHUNKREQUEST = DESCRIPTOR.message_types_by_name['UploadChunkRequest']
_UPLOADCHUNKRESPONSE = DESCRIPTOR.message_types_by_name['UploadChunkResponse']
_CREATEDATASETPROFILEREQUEST = DESCRIPTOR.message_types_by_name['CreateDatasetProfileRequest']
_CREATEDATASETPROFILERESPONSE = DESCRIPTOR.message_types_by_name['CreateDatasetProfileResponse']
_CREATECOLUMNPROFILEREQUEST = DESCRIPTOR.message_types_by_name['CreateColumnProfileRequest']
_CREATECOLUMNPROFILERESPONSE = DESCRIPTOR.message_types_by_name['CreateColumnProfileResponse']
_GETDATASETPROFILEREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetProfileRequest']
_GETDATASETPROFILERESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetProfileResponse']
_COMPAREDATASETSREQUEST = DESCRIPTOR.message_types_by_name['CompareDatasetsRequest']
_COMPAREDATASETSRESPONSE = DESCRIPTOR.message_types_by_name['CompareDatasetsResponse']
_GENERATEDATASETREQUEST = DESCRIPTOR.message_types_by_name['GenerateDatasetRequest']
_GENERATEDATASETRESPONSE = DESCRIPTOR.message_types_by_name['GenerateDatasetResponse']
_VALIDATEDATASETREQUEST = DESCRIPTOR.message_types_by_name['ValidateDatasetRequest']
_VALIDATEDATASETRESPONSE = DESCRIPTOR.message_types_by_name['ValidateDatasetResponse']
_DOWNLOADDATASETREQUEST = DESCRIPTOR.message_types_by_name['DownloadDatasetRequest']
_DOWNLOADDATASETRESPONSE = DESCRIPTOR.message_types_by_name['DownloadDatasetResponse']
_GETDATABASESREQUEST = DESCRIPTOR.message_types_by_name['GetDatabasesRequest']
_GETDATABASESRESPONSE = DESCRIPTOR.message_types_by_name['GetDatabasesResponse']
_GETTABLESREQUEST = DESCRIPTOR.message_types_by_name['GetTablesRequest']
_GETTABLESRESPONSE = DESCRIPTOR.message_types_by_name['GetTablesResponse']
_EXECUTESQLREQUEST = DESCRIPTOR.message_types_by_name['ExecuteSqlRequest']
_EXECUTESQLRESPONSE = DESCRIPTOR.message_types_by_name['ExecuteSqlResponse']
_SNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name['SnapshotRequest']
_SNAPSHOTRESPONSE = DESCRIPTOR.message_types_by_name['SnapshotResponse']
ListDatasetsRequest = _reflection.GeneratedProtocolMessageType('ListDatasetsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTDATASETSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.ListDatasetsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTDATASETSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.ListDatasetsRequest)
  })
_sym_db.RegisterMessage(ListDatasetsRequest)
_sym_db.RegisterMessage(ListDatasetsRequest.LabelsEntry)

ListDatasetsResponse = _reflection.GeneratedProtocolMessageType('ListDatasetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATASETSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.ListDatasetsResponse)
  })
_sym_db.RegisterMessage(ListDatasetsResponse)

GetDatasetRequest = _reflection.GeneratedProtocolMessageType('GetDatasetRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETDATASETREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _GETDATASETREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetRequest)
  })
_sym_db.RegisterMessage(GetDatasetRequest)
_sym_db.RegisterMessage(GetDatasetRequest.LabelsEntry)

GetDatasetResponse = _reflection.GeneratedProtocolMessageType('GetDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetResponse)
  })
_sym_db.RegisterMessage(GetDatasetResponse)

CreateDatasetRequest = _reflection.GeneratedProtocolMessageType('CreateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetRequest)
  })
_sym_db.RegisterMessage(CreateDatasetRequest)

CreateDatasetResponse = _reflection.GeneratedProtocolMessageType('CreateDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetResponse)
  })
_sym_db.RegisterMessage(CreateDatasetResponse)

UpdateDatasetRequest = _reflection.GeneratedProtocolMessageType('UpdateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASETREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.UpdateDatasetRequest)
  })
_sym_db.RegisterMessage(UpdateDatasetRequest)

UpdateDatasetResponse = _reflection.GeneratedProtocolMessageType('UpdateDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASETRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.UpdateDatasetResponse)
  })
_sym_db.RegisterMessage(UpdateDatasetResponse)

DeleteDatasetRequest = _reflection.GeneratedProtocolMessageType('DeleteDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.DeleteDatasetRequest)
  })
_sym_db.RegisterMessage(DeleteDatasetRequest)

DeleteDatasetResponse = _reflection.GeneratedProtocolMessageType('DeleteDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.DeleteDatasetResponse)
  })
_sym_db.RegisterMessage(DeleteDatasetResponse)

UploadChunkRequest = _reflection.GeneratedProtocolMessageType('UploadChunkRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCHUNKREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.UploadChunkRequest)
  })
_sym_db.RegisterMessage(UploadChunkRequest)

UploadChunkResponse = _reflection.GeneratedProtocolMessageType('UploadChunkResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCHUNKRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.UploadChunkResponse)
  })
_sym_db.RegisterMessage(UploadChunkResponse)

CreateDatasetProfileRequest = _reflection.GeneratedProtocolMessageType('CreateDatasetProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETPROFILEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetProfileRequest)
  })
_sym_db.RegisterMessage(CreateDatasetProfileRequest)

CreateDatasetProfileResponse = _reflection.GeneratedProtocolMessageType('CreateDatasetProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETPROFILERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CreateDatasetProfileResponse)
  })
_sym_db.RegisterMessage(CreateDatasetProfileResponse)

CreateColumnProfileRequest = _reflection.GeneratedProtocolMessageType('CreateColumnProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOLUMNPROFILEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CreateColumnProfileRequest)
  })
_sym_db.RegisterMessage(CreateColumnProfileRequest)

CreateColumnProfileResponse = _reflection.GeneratedProtocolMessageType('CreateColumnProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOLUMNPROFILERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CreateColumnProfileResponse)
  })
_sym_db.RegisterMessage(CreateColumnProfileResponse)

GetDatasetProfileRequest = _reflection.GeneratedProtocolMessageType('GetDatasetProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETPROFILEREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetProfileRequest)
  })
_sym_db.RegisterMessage(GetDatasetProfileRequest)

GetDatasetProfileResponse = _reflection.GeneratedProtocolMessageType('GetDatasetProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETPROFILERESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetDatasetProfileResponse)
  })
_sym_db.RegisterMessage(GetDatasetProfileResponse)

CompareDatasetsRequest = _reflection.GeneratedProtocolMessageType('CompareDatasetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREDATASETSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CompareDatasetsRequest)
  })
_sym_db.RegisterMessage(CompareDatasetsRequest)

CompareDatasetsResponse = _reflection.GeneratedProtocolMessageType('CompareDatasetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPAREDATASETSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.CompareDatasetsResponse)
  })
_sym_db.RegisterMessage(CompareDatasetsResponse)

GenerateDatasetRequest = _reflection.GeneratedProtocolMessageType('GenerateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEDATASETREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GenerateDatasetRequest)
  })
_sym_db.RegisterMessage(GenerateDatasetRequest)

GenerateDatasetResponse = _reflection.GeneratedProtocolMessageType('GenerateDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEDATASETRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GenerateDatasetResponse)
  })
_sym_db.RegisterMessage(GenerateDatasetResponse)

ValidateDatasetRequest = _reflection.GeneratedProtocolMessageType('ValidateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEDATASETREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.ValidateDatasetRequest)
  })
_sym_db.RegisterMessage(ValidateDatasetRequest)

ValidateDatasetResponse = _reflection.GeneratedProtocolMessageType('ValidateDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEDATASETRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.ValidateDatasetResponse)
  })
_sym_db.RegisterMessage(ValidateDatasetResponse)

DownloadDatasetRequest = _reflection.GeneratedProtocolMessageType('DownloadDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADDATASETREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.DownloadDatasetRequest)
  })
_sym_db.RegisterMessage(DownloadDatasetRequest)

DownloadDatasetResponse = _reflection.GeneratedProtocolMessageType('DownloadDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADDATASETRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.DownloadDatasetResponse)
  })
_sym_db.RegisterMessage(DownloadDatasetResponse)

GetDatabasesRequest = _reflection.GeneratedProtocolMessageType('GetDatabasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATABASESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetDatabasesRequest)
  })
_sym_db.RegisterMessage(GetDatabasesRequest)

GetDatabasesResponse = _reflection.GeneratedProtocolMessageType('GetDatabasesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATABASESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetDatabasesResponse)
  })
_sym_db.RegisterMessage(GetDatabasesResponse)

GetTablesRequest = _reflection.GeneratedProtocolMessageType('GetTablesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTABLESREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetTablesRequest)
  })
_sym_db.RegisterMessage(GetTablesRequest)

GetTablesResponse = _reflection.GeneratedProtocolMessageType('GetTablesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTABLESRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.GetTablesResponse)
  })
_sym_db.RegisterMessage(GetTablesResponse)

ExecuteSqlRequest = _reflection.GeneratedProtocolMessageType('ExecuteSqlRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTESQLREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.ExecuteSqlRequest)
  })
_sym_db.RegisterMessage(ExecuteSqlRequest)

ExecuteSqlResponse = _reflection.GeneratedProtocolMessageType('ExecuteSqlResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTESQLRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.ExecuteSqlResponse)
  })
_sym_db.RegisterMessage(ExecuteSqlResponse)

SnapshotRequest = _reflection.GeneratedProtocolMessageType('SnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.SnapshotRequest)
  })
_sym_db.RegisterMessage(SnapshotRequest)

SnapshotResponse = _reflection.GeneratedProtocolMessageType('SnapshotResponse', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.dataset.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.dataset.v1.SnapshotResponse)
  })
_sym_db.RegisterMessage(SnapshotResponse)

_DATASETSERVICE = DESCRIPTOR.services_by_name['DatasetService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/metaprov/modelaapi/services/dataset/v1'
  _LISTDATASETSREQUEST_LABELSENTRY._options = None
  _LISTDATASETSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _GETDATASETREQUEST_LABELSENTRY._options = None
  _GETDATASETREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _DATASETSERVICE.methods_by_name['ListDatasets']._options = None
  _DATASETSERVICE.methods_by_name['ListDatasets']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/datasets/{namespace}'
  _DATASETSERVICE.methods_by_name['GetDataset']._options = None
  _DATASETSERVICE.methods_by_name['GetDataset']._serialized_options = b'\202\323\344\223\002!\022\037/v1/datasets/{namespace}/{name}'
  _DATASETSERVICE.methods_by_name['CreateDataset']._options = None
  _DATASETSERVICE.methods_by_name['CreateDataset']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/datasets:\001*'
  _DATASETSERVICE.methods_by_name['UpdateDataset']._options = None
  _DATASETSERVICE.methods_by_name['UpdateDataset']._serialized_options = b'\202\323\344\223\002F\032A/v1/datasets/{dataset.metadata.namespace}/{dataset.metadata.name}:\001*'
  _DATASETSERVICE.methods_by_name['DeleteDataset']._options = None
  _DATASETSERVICE.methods_by_name['DeleteDataset']._serialized_options = b'\202\323\344\223\002\025*\023/v1/datasets/{name}'
  _DATASETSERVICE.methods_by_name['CompareDatasets']._options = None
  _DATASETSERVICE.methods_by_name['CompareDatasets']._serialized_options = b'\202\323\344\223\002*\"(/v1/datasets/{namespace}/{names}:compare'
  _DATASETSERVICE.methods_by_name['GetDatasetProfile']._options = None
  _DATASETSERVICE.methods_by_name['GetDatasetProfile']._serialized_options = b'\202\323\344\223\002)\022\'/v1/datasets/{namespace}/{name}:profile'
  _DATASETSERVICE.methods_by_name['CreateDatasetProfile']._options = None
  _DATASETSERVICE.methods_by_name['CreateDatasetProfile']._serialized_options = b'\202\323\344\223\002)\"\'/v1/datasets/{namespace}/{name}:profile'
  _DATASETSERVICE.methods_by_name['CreateColumnProfile']._options = None
  _DATASETSERVICE.methods_by_name['CreateColumnProfile']._serialized_options = b'\202\323\344\223\002,\"*/v1/datasets/{namespace}/{name}/columnplot'
  _DATASETSERVICE.methods_by_name['GenerateDataset']._options = None
  _DATASETSERVICE.methods_by_name['GenerateDataset']._serialized_options = b'\202\323\344\223\002+\")/v1/datasets/{namespace}/{names}:generate'
  _DATASETSERVICE.methods_by_name['ValidateDataset']._options = None
  _DATASETSERVICE.methods_by_name['ValidateDataset']._serialized_options = b'\202\323\344\223\002+\")/v1/datasets/{namespace}/{names}:validate'
  _DATASETSERVICE.methods_by_name['DownloadDataset']._options = None
  _DATASETSERVICE.methods_by_name['DownloadDataset']._serialized_options = b'\202\323\344\223\002*\"(/v1/datasets/{namespace}/{name}:download'
  _DATASETSERVICE.methods_by_name['GetDatabases']._options = None
  _DATASETSERVICE.methods_by_name['GetDatabases']._serialized_options = b'\202\323\344\223\002?\022=/v1/datasets/{connectionNamespace}/{connectionName}:databases'
  _DATASETSERVICE.methods_by_name['GetTables']._options = None
  _DATASETSERVICE.methods_by_name['GetTables']._serialized_options = b'\202\323\344\223\002<\022:/v1/datasets/{connectionNamespace}/{connectionName}:tables'
  _DATASETSERVICE.methods_by_name['ExecuteSql']._options = None
  _DATASETSERVICE.methods_by_name['ExecuteSql']._serialized_options = b'\202\323\344\223\002@\">/v1/datasets/{connectionNamespace}/{connectionName}:executesql'
  _LISTDATASETSREQUEST._serialized_start=345
  _LISTDATASETSREQUEST._serialized_end=589
  _LISTDATASETSREQUEST_LABELSENTRY._serialized_start=544
  _LISTDATASETSREQUEST_LABELSENTRY._serialized_end=589
  _LISTDATASETSRESPONSE._serialized_start=592
  _LISTDATASETSRESPONSE._serialized_end=724
  _GETDATASETREQUEST._serialized_start=727
  _GETDATASETREQUEST._serialized_end=924
  _GETDATASETREQUEST_LABELSENTRY._serialized_start=544
  _GETDATASETREQUEST_LABELSENTRY._serialized_end=589
  _GETDATASETRESPONSE._serialized_start=926
  _GETDATASETRESPONSE._serialized_end=1040
  _CREATEDATASETREQUEST._serialized_start=1042
  _CREATEDATASETREQUEST._serialized_end=1144
  _CREATEDATASETRESPONSE._serialized_start=1146
  _CREATEDATASETRESPONSE._serialized_end=1169
  _UPDATEDATASETREQUEST._serialized_start=1172
  _UPDATEDATASETREQUEST._serialized_end=1322
  _UPDATEDATASETRESPONSE._serialized_start=1324
  _UPDATEDATASETRESPONSE._serialized_end=1347
  _DELETEDATASETREQUEST._serialized_start=1349
  _DELETEDATASETREQUEST._serialized_end=1404
  _DELETEDATASETRESPONSE._serialized_start=1406
  _DELETEDATASETRESPONSE._serialized_end=1429
  _UPLOADCHUNKREQUEST._serialized_start=1431
  _UPLOADCHUNKREQUEST._serialized_end=1512
  _UPLOADCHUNKRESPONSE._serialized_start=1514
  _UPLOADCHUNKRESPONSE._serialized_end=1562
  _CREATEDATASETPROFILEREQUEST._serialized_start=1565
  _CREATEDATASETPROFILEREQUEST._serialized_end=1707
  _CREATEDATASETPROFILERESPONSE._serialized_start=1709
  _CREATEDATASETPROFILERESPONSE._serialized_end=1835
  _CREATECOLUMNPROFILEREQUEST._serialized_start=1838
  _CREATECOLUMNPROFILEREQUEST._serialized_end=1992
  _CREATECOLUMNPROFILERESPONSE._serialized_start=1994
  _CREATECOLUMNPROFILERESPONSE._serialized_end=2107
  _GETDATASETPROFILEREQUEST._serialized_start=2109
  _GETDATASETPROFILEREQUEST._serialized_end=2181
  _GETDATASETPROFILERESPONSE._serialized_start=2184
  _GETDATASETPROFILERESPONSE._serialized_end=2327
  _COMPAREDATASETSREQUEST._serialized_start=2329
  _COMPAREDATASETSREQUEST._serialized_end=2387
  _COMPAREDATASETSRESPONSE._serialized_start=2390
  _COMPAREDATASETSRESPONSE._serialized_end=2533
  _GENERATEDATASETREQUEST._serialized_start=2535
  _GENERATEDATASETREQUEST._serialized_end=2593
  _GENERATEDATASETRESPONSE._serialized_start=2596
  _GENERATEDATASETRESPONSE._serialized_end=2739
  _VALIDATEDATASETREQUEST._serialized_start=2741
  _VALIDATEDATASETREQUEST._serialized_end=2799
  _VALIDATEDATASETRESPONSE._serialized_start=2802
  _VALIDATEDATASETRESPONSE._serialized_end=2945
  _DOWNLOADDATASETREQUEST._serialized_start=2947
  _DOWNLOADDATASETREQUEST._serialized_end=3004
  _DOWNLOADDATASETRESPONSE._serialized_start=3006
  _DOWNLOADDATASETRESPONSE._serialized_end=3044
  _GETDATABASESREQUEST._serialized_start=3046
  _GETDATABASESREQUEST._serialized_end=3120
  _GETDATABASESRESPONSE._serialized_start=3122
  _GETDATABASESRESPONSE._serialized_end=3163
  _GETTABLESREQUEST._serialized_start=3165
  _GETTABLESREQUEST._serialized_end=3258
  _GETTABLESRESPONSE._serialized_start=3260
  _GETTABLESRESPONSE._serialized_end=3295
  _EXECUTESQLREQUEST._serialized_start=3297
  _EXECUTESQLREQUEST._serialized_end=3404
  _EXECUTESQLRESPONSE._serialized_start=3406
  _EXECUTESQLRESPONSE._serialized_end=3506
  _SNAPSHOTREQUEST._serialized_start=3508
  _SNAPSHOTREQUEST._serialized_end=3613
  _SNAPSHOTRESPONSE._serialized_start=3615
  _SNAPSHOTRESPONSE._serialized_end=3663
  _DATASETSERVICE._serialized_start=3666
  _DATASETSERVICE._serialized_end=6966
# @@protoc_insertion_point(module_scope)
