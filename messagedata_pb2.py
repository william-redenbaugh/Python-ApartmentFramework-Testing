# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messagedata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messagedata.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11messagedata.proto\"\xb9\x01\n\x0bMessageData\x12\x14\n\x0cmessage_size\x18\x01 \x01(\r\x12.\n\x0cmessage_type\x18\x02 \x01(\x0e\x32\x18.MessageData.MessageType\"d\n\x0bMessageType\x12\x18\n\x14GENERAL_INSTRUCTIONS\x10\x00\x12\x0f\n\x0bMATRIX_DATA\x10\x01\x12\x12\n\x0eLED_STRIP_DATA\x10\x02\x12\x16\n\x12HEAAT_CONTROL_DATA\x10\x03\x62\x06proto3')
)



_MESSAGEDATA_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='MessageData.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GENERAL_INSTRUCTIONS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATRIX_DATA', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_STRIP_DATA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAAT_CONTROL_DATA', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=107,
  serialized_end=207,
)
_sym_db.RegisterEnumDescriptor(_MESSAGEDATA_MESSAGETYPE)


_MESSAGEDATA = _descriptor.Descriptor(
  name='MessageData',
  full_name='MessageData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_size', full_name='MessageData.message_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='MessageData.message_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGEDATA_MESSAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=207,
)

_MESSAGEDATA.fields_by_name['message_type'].enum_type = _MESSAGEDATA_MESSAGETYPE
_MESSAGEDATA_MESSAGETYPE.containing_type = _MESSAGEDATA
DESCRIPTOR.message_types_by_name['MessageData'] = _MESSAGEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageData = _reflection.GeneratedProtocolMessageType('MessageData', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEDATA,
  __module__ = 'messagedata_pb2'
  # @@protoc_insertion_point(class_scope:MessageData)
  ))
_sym_db.RegisterMessage(MessageData)


# @@protoc_insertion_point(module_scope)
