# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/post_processing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import calibration_pb2 as object__detection_dot_protos_dot_calibration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/post_processing.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-object_detection/protos/post_processing.proto\x12\x17object_detection.protos\x1a)object_detection/protos/calibration.proto\"\xc9\x03\n\x16\x42\x61tchNonMaxSuppression\x12\x1a\n\x0fscore_threshold\x18\x01 \x01(\x02:\x01\x30\x12\x1a\n\riou_threshold\x18\x02 \x01(\x02:\x03\x30.6\x12%\n\x18max_detections_per_class\x18\x03 \x01(\x05:\x03\x31\x30\x30\x12!\n\x14max_total_detections\x18\x05 \x01(\x05:\x03\x31\x30\x30\x12 \n\x11use_static_shapes\x18\x06 \x01(\x08:\x05\x66\x61lse\x12%\n\x16use_class_agnostic_nms\x18\x07 \x01(\x08:\x05\x66\x61lse\x12$\n\x19max_classes_per_detection\x18\x08 \x01(\x05:\x01\x31\x12\x19\n\x0esoft_nms_sigma\x18\t \x01(\x02:\x01\x30\x12\"\n\x13use_partitioned_nms\x18\n \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10use_combined_nms\x18\x0b \x01(\x08:\x05\x66\x61lse\x12%\n\x17\x63hange_coordinate_frame\x18\x0c \x01(\x08:\x04true\x12\x1b\n\x0cuse_hard_nms\x18\r \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0buse_cpu_nms\x18\x0e \x01(\x08:\x05\x66\x61lse\"\xd9\x02\n\x0ePostProcessing\x12R\n\x19\x62\x61tch_non_max_suppression\x18\x01 \x01(\x0b\x32/.object_detection.protos.BatchNonMaxSuppression\x12Y\n\x0fscore_converter\x18\x02 \x01(\x0e\x32\x36.object_detection.protos.PostProcessing.ScoreConverter:\x08IDENTITY\x12\x16\n\x0blogit_scale\x18\x03 \x01(\x02:\x01\x31\x12\x46\n\x12\x63\x61libration_config\x18\x04 \x01(\x0b\x32*.object_detection.protos.CalibrationConfig\"8\n\x0eScoreConverter\x12\x0c\n\x08IDENTITY\x10\x00\x12\x0b\n\x07SIGMOID\x10\x01\x12\x0b\n\x07SOFTMAX\x10\x02'
  ,
  dependencies=[object__detection_dot_protos_dot_calibration__pb2.DESCRIPTOR,])



_POSTPROCESSING_SCORECONVERTER = _descriptor.EnumDescriptor(
  name='ScoreConverter',
  full_name='object_detection.protos.PostProcessing.ScoreConverter',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDENTITY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIGMOID', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOFTMAX', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=867,
  serialized_end=923,
)
_sym_db.RegisterEnumDescriptor(_POSTPROCESSING_SCORECONVERTER)


_BATCHNONMAXSUPPRESSION = _descriptor.Descriptor(
  name='BatchNonMaxSuppression',
  full_name='object_detection.protos.BatchNonMaxSuppression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='score_threshold', full_name='object_detection.protos.BatchNonMaxSuppression.score_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iou_threshold', full_name='object_detection.protos.BatchNonMaxSuppression.iou_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.6),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_detections_per_class', full_name='object_detection.protos.BatchNonMaxSuppression.max_detections_per_class', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_total_detections', full_name='object_detection.protos.BatchNonMaxSuppression.max_total_detections', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_static_shapes', full_name='object_detection.protos.BatchNonMaxSuppression.use_static_shapes', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_class_agnostic_nms', full_name='object_detection.protos.BatchNonMaxSuppression.use_class_agnostic_nms', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_classes_per_detection', full_name='object_detection.protos.BatchNonMaxSuppression.max_classes_per_detection', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='soft_nms_sigma', full_name='object_detection.protos.BatchNonMaxSuppression.soft_nms_sigma', index=7,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_partitioned_nms', full_name='object_detection.protos.BatchNonMaxSuppression.use_partitioned_nms', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_combined_nms', full_name='object_detection.protos.BatchNonMaxSuppression.use_combined_nms', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change_coordinate_frame', full_name='object_detection.protos.BatchNonMaxSuppression.change_coordinate_frame', index=10,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_hard_nms', full_name='object_detection.protos.BatchNonMaxSuppression.use_hard_nms', index=11,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_cpu_nms', full_name='object_detection.protos.BatchNonMaxSuppression.use_cpu_nms', index=12,
      number=14, type=8, cpp_type=7, label=1,
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
  ],
  serialized_start=118,
  serialized_end=575,
)


_POSTPROCESSING = _descriptor.Descriptor(
  name='PostProcessing',
  full_name='object_detection.protos.PostProcessing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_non_max_suppression', full_name='object_detection.protos.PostProcessing.batch_non_max_suppression', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score_converter', full_name='object_detection.protos.PostProcessing.score_converter', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logit_scale', full_name='object_detection.protos.PostProcessing.logit_scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='calibration_config', full_name='object_detection.protos.PostProcessing.calibration_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POSTPROCESSING_SCORECONVERTER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=923,
)

_POSTPROCESSING.fields_by_name['batch_non_max_suppression'].message_type = _BATCHNONMAXSUPPRESSION
_POSTPROCESSING.fields_by_name['score_converter'].enum_type = _POSTPROCESSING_SCORECONVERTER
_POSTPROCESSING.fields_by_name['calibration_config'].message_type = object__detection_dot_protos_dot_calibration__pb2._CALIBRATIONCONFIG
_POSTPROCESSING_SCORECONVERTER.containing_type = _POSTPROCESSING
DESCRIPTOR.message_types_by_name['BatchNonMaxSuppression'] = _BATCHNONMAXSUPPRESSION
DESCRIPTOR.message_types_by_name['PostProcessing'] = _POSTPROCESSING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchNonMaxSuppression = _reflection.GeneratedProtocolMessageType('BatchNonMaxSuppression', (_message.Message,), {
  'DESCRIPTOR' : _BATCHNONMAXSUPPRESSION,
  '__module__' : 'object_detection.protos.post_processing_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.BatchNonMaxSuppression)
  })
_sym_db.RegisterMessage(BatchNonMaxSuppression)

PostProcessing = _reflection.GeneratedProtocolMessageType('PostProcessing', (_message.Message,), {
  'DESCRIPTOR' : _POSTPROCESSING,
  '__module__' : 'object_detection.protos.post_processing_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.PostProcessing)
  })
_sym_db.RegisterMessage(PostProcessing)


# @@protoc_insertion_point(module_scope)
