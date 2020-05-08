import serial
import messagedata_pb2
import general_instructions_pb2
import time

# Setting up the serial device.
ser = serial.Serial("COM4", 115200, serial.EIGHTBITS, serial.PARITY_NONE)

# Intruction that tells microcontroller to toggle LED.
general_instruction_data = general_instructions_pb2.GeneralInstructions()
general_instruction_data.main_instructions = general_instructions_pb2.GeneralInstructions.MainInstrEnum.FLASH_LED
instruction_bytearray = bytearray(general_instruction_data.SerializeToString())

# Setting up message and general instruction data to tell led to toggle led.
message_data = messagedata_pb2.MessageData()
message_data.message_size = len(instruction_bytearray)
message_data.message_type = messagedata_pb2.MessageData.MessageType.GENERAL_INSTRUCTIONS

msg_dat = bytearray(message_data.SerializeToString())
msg_len = 16 - len(msg_dat)

# To ensure that our first message is always 16 bytes we append whatever remainder bytes
# are left.
for i in range(msg_len):
    msg_dat.append(0)

# Then we tack on the last instruction
msg = msg_dat + instruction_bytearray

for val in msg:
    print(int(val))

for i in range(100):
    ser.write(msg)
    time.sleep(.01)