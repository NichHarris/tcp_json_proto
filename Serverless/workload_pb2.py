# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='workload.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eworkload.proto\"T\n\x0bWorkloadRFD\x12\x0e\n\x06rfw_id\x18\x01 \x01(\t\x12\x15\n\rlast_batch_id\x18\x02 \x01(\x05\x12\x1e\n\x16requested_data_samples\x18\x03 \x03(\x02\"\x9b\x01\n\x0bWorkloadRFW\x12\x0e\n\x06rfw_id\x18\x01 \x01(\x05\x12\x16\n\x0e\x62\x65nchmark_type\x18\x02 \x01(\x08\x12\x17\n\x0fworkload_metric\x18\x03 \x01(\x05\x12\x12\n\nbatch_unit\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61tch_id\x18\x05 \x01(\x05\x12\x12\n\nbatch_size\x18\x06 \x01(\x05\x12\x11\n\tdata_type\x18\x07 \x01(\x08\x32\x39\n\x0fWorkloadService\x12&\n\x08Workload\x12\x0c.WorkloadRFW\x1a\x0c.WorkloadRFDb\x06proto3'
)




_WORKLOADRFD = _descriptor.Descriptor(
  name='WorkloadRFD',
  full_name='WorkloadRFD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rfw_id', full_name='WorkloadRFD.rfw_id', index=0,
      number=1, type=9, cpp_type=1, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_batch_id', full_name='WorkloadRFD.last_batch_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requested_data_samples', full_name='WorkloadRFD.requested_data_samples', index=2,
      number=3, type=2, cpp_type=6, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=102,
)


_WORKLOADRFW = _descriptor.Descriptor(
  name='WorkloadRFW',
  full_name='WorkloadRFW',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rfw_id', full_name='WorkloadRFW.rfw_id', index=0,
      number=1, type=9, cpp_type=1, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='benchmark_type', full_name='WorkloadRFW.benchmark_type', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workload_metric', full_name='WorkloadRFW.workload_metric', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_unit', full_name='WorkloadRFW.batch_unit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='WorkloadRFW.batch_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='WorkloadRFW.batch_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='WorkloadRFW.data_type', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=260,
)

DESCRIPTOR.message_types_by_name['WorkloadRFD'] = _WORKLOADRFD
DESCRIPTOR.message_types_by_name['WorkloadRFW'] = _WORKLOADRFW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkloadRFD = _reflection.GeneratedProtocolMessageType('WorkloadRFD', (_message.Message,), {
  'DESCRIPTOR' : _WORKLOADRFD,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:WorkloadRFD)
  })
_sym_db.RegisterMessage(WorkloadRFD)

WorkloadRFW = _reflection.GeneratedProtocolMessageType('WorkloadRFW', (_message.Message,), {
  'DESCRIPTOR' : _WORKLOADRFW,
  '__module__' : 'workload_pb2'
  # @@protoc_insertion_point(class_scope:WorkloadRFW)
  })
_sym_db.RegisterMessage(WorkloadRFW)



_WORKLOADSERVICE = _descriptor.ServiceDescriptor(
  name='WorkloadService',
  full_name='WorkloadService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=262,
  serialized_end=319,
  methods=[
  _descriptor.MethodDescriptor(
    name='Workload',
    full_name='WorkloadService.Workload',
    index=0,
    containing_service=None,
    input_type=_WORKLOADRFW,
    output_type=_WORKLOADRFD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKLOADSERVICE)

DESCRIPTOR.services_by_name['WorkloadService'] = _WORKLOADSERVICE

# @@protoc_insertion_point(module_scope)
