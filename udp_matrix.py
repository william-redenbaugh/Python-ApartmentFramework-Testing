import socket

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
        self.out_arr[spot + 1] = r
        self.out_arr[spot + 2] = r

    def update(self):
        # If we are using UDP sockets to send information
        msg = bytearray(self.out_arr)
        self.client_socket.sendto(msg, self.server_address_port)