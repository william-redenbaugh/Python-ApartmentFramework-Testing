import serial
import messagedata_pb2
import heaat_message_pb2
import time
import udp_matrix
import colorsys
import pyaudio

# Setting up the serial device. If we are doing serial testing
#ser = serial.Serial("COM4", 115200, serial.EIGHTBITS, serial.PARITY_NONE)
# If we are doing serial testing
# ser.write(msg)
# hey_world = "hello world"
# msg = bytes(hey_world, 'ascii');

def test_matrix_hsv():
    # Address and port for our esp32. if we are using sockets.

    server_address_port = ('192.168.1.27', 4040)
    matrix = udp_matrix.LEDMatrix(server_address_port, 64, 32)
    while True:
        for h in range(255):
            for y in range(32):
                for x in range(64):
                    hue_val = ((y * x)/20 + h * 3) % 255
                    matrix.set_led_hsv(x, y, hue_val, 255, 60)
            matrix.update()
            time.sleep(0.01)

test_matrix_hsv()