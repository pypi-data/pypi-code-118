# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/input_reader.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/input_reader.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*object_detection/protos/input_reader.proto\x12\x17object_detection.protos\"\xeb\n\n\x0bInputReader\x12\x0e\n\x04name\x18\x17 \x01(\t:\x00\x12\x18\n\x0elabel_map_path\x18\x01 \x01(\t:\x00\x12\x15\n\x07shuffle\x18\x02 \x01(\x08:\x04true\x12!\n\x13shuffle_buffer_size\x18\x0b \x01(\r:\x04\x32\x30\x34\x38\x12*\n\x1d\x66ilenames_shuffle_buffer_size\x18\x0c \x01(\r:\x03\x31\x30\x30\x12\x15\n\nnum_epochs\x18\x05 \x01(\r:\x01\x30\x12!\n\x16sample_1_of_n_examples\x18\x16 \x01(\r:\x01\x31\x12\x17\n\x0bnum_readers\x18\x06 \x01(\r:\x02\x36\x34\x12\x1f\n\x14num_parallel_batches\x18\x13 \x01(\r:\x01\x38\x12\x1f\n\x14num_prefetch_batches\x18\x14 \x01(\x05:\x01\x32\x12 \n\x0equeue_capacity\x18\x03 \x01(\r:\x04\x32\x30\x30\x30\x42\x02\x18\x01\x12#\n\x11min_after_dequeue\x18\x04 \x01(\r:\x04\x31\x30\x30\x30\x42\x02\x18\x01\x12\x1d\n\x11read_block_length\x18\x0f \x01(\r:\x02\x33\x32\x12\x1e\n\rprefetch_size\x18\r \x01(\r:\x03\x35\x31\x32\x42\x02\x18\x01\x12&\n\x16num_parallel_map_calls\x18\x0e \x01(\r:\x02\x36\x34\x42\x02\x18\x01\x12\x1c\n\x0e\x64rop_remainder\x18# \x01(\x08:\x04true\x12\"\n\x17num_additional_channels\x18\x12 \x01(\x05:\x01\x30\x12\x18\n\rnum_keypoints\x18\x10 \x01(\r:\x01\x30\x12\x1c\n\x14keypoint_type_weight\x18\x1a \x03(\x02\x12 \n\x13max_number_of_boxes\x18\x15 \x01(\x05:\x03\x31\x30\x30\x12%\n\x16load_multiclass_scores\x18\x18 \x01(\x08:\x05\x66\x61lse\x12$\n\x15load_context_features\x18\x19 \x01(\x08:\x05\x66\x61lse\x12%\n\x16load_context_image_ids\x18$ \x01(\x08:\x05\x66\x61lse\x12\"\n\x13load_instance_masks\x18\x07 \x01(\x08:\x05\x66\x61lse\x12M\n\tmask_type\x18\n \x01(\x0e\x32).object_detection.protos.InstanceMaskType:\x0fNUMERICAL_MASKS\x12\x1e\n\x0fload_dense_pose\x18\x1f \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rload_track_id\x18! \x01(\x08:\x05\x66\x61lse\x12+\n\x1cload_keypoint_depth_features\x18% \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10use_display_name\x18\x11 \x01(\x08:\x05\x66\x61lse\x12 \n\x11include_source_id\x18\x1b \x01(\x08:\x05\x66\x61lse\x12\x42\n\ninput_type\x18\x1e \x01(\x0e\x32\".object_detection.protos.InputType:\nTF_EXAMPLE\x12\x17\n\x0b\x66rame_index\x18  \x01(\x05:\x02-1\x12N\n\x16tf_record_input_reader\x18\x08 \x01(\x0b\x32,.object_detection.protos.TFRecordInputReaderH\x00\x12M\n\x15\x65xternal_input_reader\x18\t \x01(\x0b\x32,.object_detection.protos.ExternalInputReaderH\x00\x12$\n\x1csample_from_datasets_weights\x18\" \x03(\x02\x12&\n\x17\x65xpand_labels_hierarchy\x18\x1d \x01(\x08:\x05\x66\x61lseB\x0e\n\x0cinput_reader\")\n\x13TFRecordInputReader\x12\x12\n\ninput_path\x18\x01 \x03(\t\"\x1c\n\x13\x45xternalInputReader*\x05\x08\x01\x10\xe8\x07*C\n\x10InstanceMaskType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x13\n\x0fNUMERICAL_MASKS\x10\x01\x12\r\n\tPNG_MASKS\x10\x02*G\n\tInputType\x12\x11\n\rINPUT_DEFAULT\x10\x00\x12\x0e\n\nTF_EXAMPLE\x10\x01\x12\x17\n\x13TF_SEQUENCE_EXAMPLE\x10\x02'
)

_INSTANCEMASKTYPE = _descriptor.EnumDescriptor(
  name='InstanceMaskType',
  full_name='object_detection.protos.InstanceMaskType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NUMERICAL_MASKS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PNG_MASKS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1534,
  serialized_end=1601,
)
_sym_db.RegisterEnumDescriptor(_INSTANCEMASKTYPE)

InstanceMaskType = enum_type_wrapper.EnumTypeWrapper(_INSTANCEMASKTYPE)
_INPUTTYPE = _descriptor.EnumDescriptor(
  name='InputType',
  full_name='object_detection.protos.InputType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INPUT_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TF_EXAMPLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TF_SEQUENCE_EXAMPLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1603,
  serialized_end=1674,
)
_sym_db.RegisterEnumDescriptor(_INPUTTYPE)

InputType = enum_type_wrapper.EnumTypeWrapper(_INPUTTYPE)
DEFAULT = 0
NUMERICAL_MASKS = 1
PNG_MASKS = 2
INPUT_DEFAULT = 0
TF_EXAMPLE = 1
TF_SEQUENCE_EXAMPLE = 2



_INPUTREADER = _descriptor.Descriptor(
  name='InputReader',
  full_name='object_detection.protos.InputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='object_detection.protos.InputReader.name', index=0,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_map_path', full_name='object_detection.protos.InputReader.label_map_path', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shuffle', full_name='object_detection.protos.InputReader.shuffle', index=2,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shuffle_buffer_size', full_name='object_detection.protos.InputReader.shuffle_buffer_size', index=3,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2048,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filenames_shuffle_buffer_size', full_name='object_detection.protos.InputReader.filenames_shuffle_buffer_size', index=4,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_epochs', full_name='object_detection.protos.InputReader.num_epochs', index=5,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_1_of_n_examples', full_name='object_detection.protos.InputReader.sample_1_of_n_examples', index=6,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_readers', full_name='object_detection.protos.InputReader.num_readers', index=7,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=64,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_parallel_batches', full_name='object_detection.protos.InputReader.num_parallel_batches', index=8,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_prefetch_batches', full_name='object_detection.protos.InputReader.num_prefetch_batches', index=9,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queue_capacity', full_name='object_detection.protos.InputReader.queue_capacity', index=10,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_after_dequeue', full_name='object_detection.protos.InputReader.min_after_dequeue', index=11,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_block_length', full_name='object_detection.protos.InputReader.read_block_length', index=12,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefetch_size', full_name='object_detection.protos.InputReader.prefetch_size', index=13,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=512,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_parallel_map_calls', full_name='object_detection.protos.InputReader.num_parallel_map_calls', index=14,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=64,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drop_remainder', full_name='object_detection.protos.InputReader.drop_remainder', index=15,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_additional_channels', full_name='object_detection.protos.InputReader.num_additional_channels', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_keypoints', full_name='object_detection.protos.InputReader.num_keypoints', index=17,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keypoint_type_weight', full_name='object_detection.protos.InputReader.keypoint_type_weight', index=18,
      number=26, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_number_of_boxes', full_name='object_detection.protos.InputReader.max_number_of_boxes', index=19,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_multiclass_scores', full_name='object_detection.protos.InputReader.load_multiclass_scores', index=20,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_context_features', full_name='object_detection.protos.InputReader.load_context_features', index=21,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_context_image_ids', full_name='object_detection.protos.InputReader.load_context_image_ids', index=22,
      number=36, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_instance_masks', full_name='object_detection.protos.InputReader.load_instance_masks', index=23,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask_type', full_name='object_detection.protos.InputReader.mask_type', index=24,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_dense_pose', full_name='object_detection.protos.InputReader.load_dense_pose', index=25,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_track_id', full_name='object_detection.protos.InputReader.load_track_id', index=26,
      number=33, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_keypoint_depth_features', full_name='object_detection.protos.InputReader.load_keypoint_depth_features', index=27,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_display_name', full_name='object_detection.protos.InputReader.use_display_name', index=28,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_source_id', full_name='object_detection.protos.InputReader.include_source_id', index=29,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_type', full_name='object_detection.protos.InputReader.input_type', index=30,
      number=30, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame_index', full_name='object_detection.protos.InputReader.frame_index', index=31,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tf_record_input_reader', full_name='object_detection.protos.InputReader.tf_record_input_reader', index=32,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='external_input_reader', full_name='object_detection.protos.InputReader.external_input_reader', index=33,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_from_datasets_weights', full_name='object_detection.protos.InputReader.sample_from_datasets_weights', index=34,
      number=34, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expand_labels_hierarchy', full_name='object_detection.protos.InputReader.expand_labels_hierarchy', index=35,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='input_reader', full_name='object_detection.protos.InputReader.input_reader',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=72,
  serialized_end=1459,
)


_TFRECORDINPUTREADER = _descriptor.Descriptor(
  name='TFRecordInputReader',
  full_name='object_detection.protos.TFRecordInputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_path', full_name='object_detection.protos.TFRecordInputReader.input_path', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1461,
  serialized_end=1502,
)


_EXTERNALINPUTREADER = _descriptor.Descriptor(
  name='ExternalInputReader',
  full_name='object_detection.protos.ExternalInputReader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1, 1000), ],
  oneofs=[
  ],
  serialized_start=1504,
  serialized_end=1532,
)

_INPUTREADER.fields_by_name['mask_type'].enum_type = _INSTANCEMASKTYPE
_INPUTREADER.fields_by_name['input_type'].enum_type = _INPUTTYPE
_INPUTREADER.fields_by_name['tf_record_input_reader'].message_type = _TFRECORDINPUTREADER
_INPUTREADER.fields_by_name['external_input_reader'].message_type = _EXTERNALINPUTREADER
_INPUTREADER.oneofs_by_name['input_reader'].fields.append(
  _INPUTREADER.fields_by_name['tf_record_input_reader'])
_INPUTREADER.fields_by_name['tf_record_input_reader'].containing_oneof = _INPUTREADER.oneofs_by_name['input_reader']
_INPUTREADER.oneofs_by_name['input_reader'].fields.append(
  _INPUTREADER.fields_by_name['external_input_reader'])
_INPUTREADER.fields_by_name['external_input_reader'].containing_oneof = _INPUTREADER.oneofs_by_name['input_reader']
DESCRIPTOR.message_types_by_name['InputReader'] = _INPUTREADER
DESCRIPTOR.message_types_by_name['TFRecordInputReader'] = _TFRECORDINPUTREADER
DESCRIPTOR.message_types_by_name['ExternalInputReader'] = _EXTERNALINPUTREADER
DESCRIPTOR.enum_types_by_name['InstanceMaskType'] = _INSTANCEMASKTYPE
DESCRIPTOR.enum_types_by_name['InputType'] = _INPUTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputReader = _reflection.GeneratedProtocolMessageType('InputReader', (_message.Message,), {
  'DESCRIPTOR' : _INPUTREADER,
  '__module__' : 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.InputReader)
  })
_sym_db.RegisterMessage(InputReader)

TFRecordInputReader = _reflection.GeneratedProtocolMessageType('TFRecordInputReader', (_message.Message,), {
  'DESCRIPTOR' : _TFRECORDINPUTREADER,
  '__module__' : 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.TFRecordInputReader)
  })
_sym_db.RegisterMessage(TFRecordInputReader)

ExternalInputReader = _reflection.GeneratedProtocolMessageType('ExternalInputReader', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALINPUTREADER,
  '__module__' : 'object_detection.protos.input_reader_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ExternalInputReader)
  })
_sym_db.RegisterMessage(ExternalInputReader)


_INPUTREADER.fields_by_name['queue_capacity']._options = None
_INPUTREADER.fields_by_name['min_after_dequeue']._options = None
_INPUTREADER.fields_by_name['prefetch_size']._options = None
_INPUTREADER.fields_by_name['num_parallel_map_calls']._options = None
# @@protoc_insertion_point(module_scope)
