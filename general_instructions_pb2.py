# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: general_instructions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='general_instructions.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ageneral_instructions.proto\"\xbf\x01\n\x13GeneralInstructions\x12=\n\x11main_instructions\x18\x01 \x01(\x0e\x32\".GeneralInstructions.MainInstrEnum\"i\n\rMainInstrEnum\x12\x0e\n\nDO_NOTHING\x10\x00\x12\n\n\x06REBOOT\x10\x01\x12\x0c\n\x08\x46REE_MEM\x10\x02\x12\r\n\tFLASH_LED\x10\x03\x12\x0f\n\x0b\x46LASH_GREEN\x10\x04\x12\x0e\n\nFLASH_BLUE\x10\x05\x62\x06proto3')
)



_GENERALINSTRUCTIONS_MAININSTRENUM = _descriptor.EnumDescriptor(
  name='MainInstrEnum',
  full_name='GeneralInstructions.MainInstrEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DO_NOTHING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REBOOT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREE_MEM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_LED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_GREEN', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_BLUE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=117,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_GENERALINSTRUCTIONS_MAININSTRENUM)


_GENERALINSTRUCTIONS = _descriptor.Descriptor(
  name='GeneralInstructions',
  full_name='GeneralInstructions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='main_instructions', full_name='GeneralInstructions.main_instructions', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GENERALINSTRUCTIONS_MAININSTRENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=222,
)

_GENERALINSTRUCTIONS.fields_by_name['main_instructions'].enum_type = _GENERALINSTRUCTIONS_MAININSTRENUM
_GENERALINSTRUCTIONS_MAININSTRENUM.containing_type = _GENERALINSTRUCTIONS
DESCRIPTOR.message_types_by_name['GeneralInstructions'] = _GENERALINSTRUCTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeneralInstructions = _reflection.GeneratedProtocolMessageType('GeneralInstructions', (_message.Message,), dict(
  DESCRIPTOR = _GENERALINSTRUCTIONS,
  __module__ = 'general_instructions_pb2'
  # @@protoc_insertion_point(class_scope:GeneralInstructions)
  ))
_sym_db.RegisterMessage(GeneralInstructions)


# @@protoc_insertion_point(module_scope)
