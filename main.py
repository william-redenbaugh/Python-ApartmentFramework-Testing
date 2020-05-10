import serial
import messagedata_pb2
import heaat_message_pb2
import time
import socket
import sys

# Setting up the serial device. If we are doing serial testing
#ser = serial.Serial("COM4", 115200, serial.EIGHTBITS, serial.PARITY_NONE)

# Address and port for our esp32. if we are using sockets.
server_address_port = ('192.168.1.3', 4040)
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

heaat_data = heaat_message_pb2.HeaatMessage()
heaat_data.red = 100
heaat_data.green = 0
heaat_data.blue = 0
heaat_data.brightness = 15
instruction_bytearray = bytearray(heaat_data.SerializeToString())

# Setting up message and general instruction data to tell led to toggle led.
message_data = messagedata_pb2.MessageData()
message_data.message_size = len(instruction_bytearray)
message_data.message_type = messagedata_pb2.MessageData.MessageType.HEAAT_CONTROL_DATA

msg_dat = bytearray(message_data.SerializeToString())
msg_len = 16 - len(msg_dat)

# To ensure that our first message is always 16 bytes we append whatever remainder bytes
# are left.
for i in range(msg_len):
    msg_dat.append(0)

# Then we tack on the last instruction
msg = msg_dat + instruction_bytearray

# If we are doing serial testing
# ser.write(msg)

# If we are using UDP sockets to send information
client_socket.sendto(msg, server_address_port)