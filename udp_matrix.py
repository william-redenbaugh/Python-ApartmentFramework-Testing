import socket
import colorsys
import messagedata_pb2

class LEDMatrix:
    def __init__(self, server_address_port,  x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.out_arr = [0] * x_size * y_size * 3

        self.server_address_port = server_address_port
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Setting up message and general instruction data to tell led to toggle led.
        self.message_data = messagedata_pb2.MessageData()
        self.message_data.message_size = 6144
        self.message_data.message_type = messagedata_pb2.MessageData.MessageType.MATRIX_DATA

        self.msg_dat = bytearray(self.message_data.SerializeToString())
        msg_len = 16 - len(self.msg_dat)
        for i in range(msg_len):
            self.msg_dat.append(0)

    def set_led(self, x, y, r, g, b):
        spot = (self.x_size * y + x) * 3
        self.out_arr[spot] = r
        self.out_arr[spot + 1] = g
        self.out_arr[spot + 2] = b

    def set_led_hsv(self, x, y, h, s, v):
        hue = h
        if hue > 255:
            hue = 255
        if hue < 0:
            hue = 0
        saturation = s
        if saturation > 255:
            saturation = 255
        if saturation < 0:
            saturation = 0
        value = v
        if value > 255:
            value = 255
        if value < 0:
            value = 0

        r, g, b = colorsys.hsv_to_rgb(hue/256, saturation/256, value/256)
        r = int(r * 256)
        g = int(g * 256)
        b = int(b * 256)
        self.set_led(x, y, r, g, b)

    def update(self):
        # If we are using UDP sockets to send information
        msg = self.msg_dat + bytearray(self.out_arr)
        self.client_socket.sendto(msg, self.server_address_port)