# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/tensor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import resource_handle_pb2 as tensorflow_dot_core_dot_framework_dot_resource__handle__pb2
from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/tensor.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\014TensorProtosP\001ZMgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/tensor_go_proto\370\001\001'),
  serialized_pb=_b('\n&tensorflow/core/framework/tensor.proto\x12\ntensorflow\x1a/tensorflow/core/framework/resource_handle.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"\x8c\x04\n\x0bTensorProto\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x32\n\x0ctensor_shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\x16\n\x0eversion_number\x18\x03 \x01(\x05\x12\x16\n\x0etensor_content\x18\x04 \x01(\x0c\x12\x14\n\x08half_val\x18\r \x03(\x05\x42\x02\x10\x01\x12\x15\n\tfloat_val\x18\x05 \x03(\x02\x42\x02\x10\x01\x12\x16\n\ndouble_val\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\x13\n\x07int_val\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x12\n\nstring_val\x18\x08 \x03(\x0c\x12\x18\n\x0cscomplex_val\x18\t \x03(\x02\x42\x02\x10\x01\x12\x15\n\tint64_val\x18\n \x03(\x03\x42\x02\x10\x01\x12\x14\n\x08\x62ool_val\x18\x0b \x03(\x08\x42\x02\x10\x01\x12\x18\n\x0c\x64\x63omplex_val\x18\x0c \x03(\x01\x42\x02\x10\x01\x12<\n\x13resource_handle_val\x18\x0e \x03(\x0b\x32\x1f.tensorflow.ResourceHandleProto\x12\x37\n\x0bvariant_val\x18\x0f \x03(\x0b\x32\".tensorflow.VariantTensorDataProto\x12\x16\n\nuint32_val\x18\x10 \x03(\rB\x02\x10\x01\x12\x16\n\nuint64_val\x18\x11 \x03(\x04\x42\x02\x10\x01\"g\n\x16VariantTensorDataProto\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x10\n\x08metadata\x18\x02 \x01(\x0c\x12(\n\x07tensors\x18\x03 \x03(\x0b\x32\x17.tensorflow.TensorProtoB|\n\x18org.tensorflow.frameworkB\x0cTensorProtosP\x01ZMgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/tensor_go_proto\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_resource__handle__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_TENSORPROTO = _descriptor.Descriptor(
  name='TensorProto',
  full_name='tensorflow.TensorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.TensorProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='tensorflow.TensorProto.tensor_shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_number', full_name='tensorflow.TensorProto.version_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_content', full_name='tensorflow.TensorProto.tensor_content', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='half_val', full_name='tensorflow.TensorProto.half_val', index=4,
      number=13, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_val', full_name='tensorflow.TensorProto.float_val', index=5,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='tensorflow.TensorProto.double_val', index=6,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='tensorflow.TensorProto.int_val', index=7,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='tensorflow.TensorProto.string_val', index=8,
      number=8, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scomplex_val', full_name='tensorflow.TensorProto.scomplex_val', index=9,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_val', full_name='tensorflow.TensorProto.int64_val', index=10,
      number=10, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_val', full_name='tensorflow.TensorProto.bool_val', index=11,
      number=11, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dcomplex_val', full_name='tensorflow.TensorProto.dcomplex_val', index=12,
      number=12, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_handle_val', full_name='tensorflow.TensorProto.resource_handle_val', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variant_val', full_name='tensorflow.TensorProto.variant_val', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32_val', full_name='tensorflow.TensorProto.uint32_val', index=15,
      number=16, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_val', full_name='tensorflow.TensorProto.uint64_val', index=16,
      number=17, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=189,
  serialized_end=713,
)


_VARIANTTENSORDATAPROTO = _descriptor.Descriptor(
  name='VariantTensorDataProto',
  full_name='tensorflow.VariantTensorDataProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_name', full_name='tensorflow.VariantTensorDataProto.type_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tensorflow.VariantTensorDataProto.metadata', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensors', full_name='tensorflow.VariantTensorDataProto.tensors', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=715,
  serialized_end=818,
)

_TENSORPROTO.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_TENSORPROTO.fields_by_name['tensor_shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_TENSORPROTO.fields_by_name['resource_handle_val'].message_type = tensorflow_dot_core_dot_framework_dot_resource__handle__pb2._RESOURCEHANDLEPROTO
_TENSORPROTO.fields_by_name['variant_val'].message_type = _VARIANTTENSORDATAPROTO
_VARIANTTENSORDATAPROTO.fields_by_name['tensors'].message_type = _TENSORPROTO
DESCRIPTOR.message_types_by_name['TensorProto'] = _TENSORPROTO
DESCRIPTOR.message_types_by_name['VariantTensorDataProto'] = _VARIANTTENSORDATAPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorProto = _reflection.GeneratedProtocolMessageType('TensorProto', (_message.Message,), {
  'DESCRIPTOR' : _TENSORPROTO,
  '__module__' : 'tensorflow.core.framework.tensor_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TensorProto)
  })
_sym_db.RegisterMessage(TensorProto)

VariantTensorDataProto = _reflection.GeneratedProtocolMessageType('VariantTensorDataProto', (_message.Message,), {
  'DESCRIPTOR' : _VARIANTTENSORDATAPROTO,
  '__module__' : 'tensorflow.core.framework.tensor_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.VariantTensorDataProto)
  })
_sym_db.RegisterMessage(VariantTensorDataProto)


DESCRIPTOR._options = None
_TENSORPROTO.fields_by_name['half_val']._options = None
_TENSORPROTO.fields_by_name['float_val']._options = None
_TENSORPROTO.fields_by_name['double_val']._options = None
_TENSORPROTO.fields_by_name['int_val']._options = None
_TENSORPROTO.fields_by_name['scomplex_val']._options = None
_TENSORPROTO.fields_by_name['int64_val']._options = None
_TENSORPROTO.fields_by_name['bool_val']._options = None
_TENSORPROTO.fields_by_name['dcomplex_val']._options = None
_TENSORPROTO.fields_by_name['uint32_val']._options = None
_TENSORPROTO.fields_by_name['uint64_val']._options = None
# @@protoc_insertion_point(module_scope)
