import socket
import colorsys

class LEDMatrix:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.out_arr = [0] * x_size * y_size * 3

        self.server_address_port = ('192.168.1.27', 4040)
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


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

        r, g, b = colorsys.hsv_to_rgb(hue/255, saturation/255, value/255)
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        self.set_led(x, y, r, g, b)

    def update(self):
        # If we are using UDP sockets to send information
        msg = bytearray(self.out_arr)
        self.client_socket.sendto(msg, self.server_address_port)