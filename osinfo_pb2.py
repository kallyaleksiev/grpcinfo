# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osinfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cosinfo.proto\x12\x06osinfo\"*\n\x06OSInfo\x12\x0e\n\x06osname\x18\x01 \x01(\t\x12\x10\n\x08totalRAM\x18\x02 \x01(\x03\"T\n\x0bProcessInfo\x12\x0b\n\x03pid\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x14\n\x0c\x63reationTime\x18\x03 \x01(\x01\x12\x10\n\x08\x63hildren\x18\x04 \x03(\x05\"\t\n\x07OSQuery\"\x1b\n\x0cProcessQuery\x12\x0b\n\x03pid\x18\x01 \x01(\x05\x32\x84\x01\n\x0eOSInfoProvider\x12.\n\tGetOSInfo\x12\x0f.osinfo.OSQuery\x1a\x0e.osinfo.OSInfo\"\x00\x12\x42\n\x0fListProcessInfo\x12\x14.osinfo.ProcessQuery\x1a\x13.osinfo.ProcessInfo\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osinfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OSINFO._serialized_start=24
  _OSINFO._serialized_end=66
  _PROCESSINFO._serialized_start=68
  _PROCESSINFO._serialized_end=152
  _OSQUERY._serialized_start=154
  _OSQUERY._serialized_end=163
  _PROCESSQUERY._serialized_start=165
  _PROCESSQUERY._serialized_end=192
  _OSINFOPROVIDER._serialized_start=195
  _OSINFOPROVIDER._serialized_end=327
# @@protoc_insertion_point(module_scope)
