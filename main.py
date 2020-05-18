import serial
import messagedata_pb2
import heaat_message_pb2

import time
import udp_matrix

# Setting up the serial device. If we are doing serial testing
#ser = serial.Serial("COM4", 115200, serial.EIGHTBITS, serial.PARITY_NONE)

def test_matrix():
    # Address and port for our esp32. if we are using sockets.
    # server_address_port = ('192.168.1.27', 4040)
    # client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    matrix = udp_matrix.LEDMatrix(64, 32)

    matrix.set_led(0, 0, 100, 100, 100)
    for x in range(64):
        for y in range(32):
            matrix.set_led(x, y, 200, 200, 200)
            matrix.update()
            time.sleep(0.01)

    matrix.update()
    #matrix = udp_matrix.UDPMatrix(64, 32)
    #matrix.set_led(20, 20, 20, 10, 10)

    '''
    instruction_bytearray = bytearray([0] * 20)
    # Setting up message and general instruction data to tell led to toggle led.
    message_data = messagedata_pb2.MessageData()
    message_data.message_size = len(instruction_bytearray)
    message_data.message_type = messagedata_pb2.MessageData.MessageType.MATRIX_DATA

    msg_dat = bytearray(message_data.SerializeToString())
    msg_len = 16 - len(msg_dat)

    # To ensure that our first message is always 16 bytes we append whatever remainder bytes
    # are left.
    for i in range(msg_len):
        msg_dat.append(0)

    # Then we tack on the last instruction
    msg = msg_dat + instruction_bytearray
    '''

    # If we are doing serial testing
    # ser.write(msg)
    # hey_world = "hello world"
    # msg = bytes(hey_world, 'ascii');


test_matrix()