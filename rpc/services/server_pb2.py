# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import rpc.services.funds_pb2 as funds__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='rpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cserver.proto\x12\x03rpc\x1a\x0b\x66unds.proto2X\n\nRpcService\x12J\n\x13\x46undCategoryHandler\x12\x18.rpc.FundCategoryRequest\x1a\x19.rpc.FundCategoryResponseb\x06proto3'
  ,
  dependencies=[funds__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RPCSERVICE = _descriptor.ServiceDescriptor(
  name='RpcService',
  full_name='rpc.RpcService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=34,
  serialized_end=122,
  methods=[
  _descriptor.MethodDescriptor(
    name='FundCategoryHandler',
    full_name='rpc.RpcService.FundCategoryHandler',
    index=0,
    containing_service=None,
    input_type=funds__pb2._FUNDCATEGORYREQUEST,
    output_type=funds__pb2._FUNDCATEGORYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPCSERVICE)

DESCRIPTOR.services_by_name['RpcService'] = _RPCSERVICE

# @@protoc_insertion_point(module_scope)