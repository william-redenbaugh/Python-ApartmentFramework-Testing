# Python Default Libraries
import serial
import colorsys
import time

# Protobuffer Messages!
import messagedata_pb2
import heaat_message_pb2
import general_instructions_pb2

# Our Python Files!
import udp_matrix
import fft

# Setting up the serial device. If we are doing serial testing
#ser = serial.Serial("COM4", 115200, serial.EIGHTBITS, serial.PARITY_NONE)
# If we are doing serial testing
# ser.write(msg)
# hey_world = "hello world"
# msg = bytes(hey_world, 'ascii');


def test_status_serial():
    # Setting up the serial device. If we are doing serial testing
    ser = serial.Serial("COM4", 115200, serial.EIGHTBITS, serial.PARITY_NONE)

    general_instructions = general_instructions_pb2.GeneralInstructions()
    general_instructions.main_instructions = general_instructions_pb2.GeneralInstructions.MainInstrEnum.FLASH_GREEN

    general_instr_byarr = bytearray(general_instructions.SerializeToString())

    # Setting up message and general instruction data to tell led to toggle led.
    message_data = messagedata_pb2.MessageData()
    message_data.message_size = len(general_instr_byarr)
    message_data.message_type = messagedata_pb2.MessageData.MessageType.GENERAL_INSTRUCTIONS

    msg_dat = bytearray(message_data.SerializeToString())
    msg_len = 16 - len(msg_dat)
    for i in range(msg_len):
        msg_dat.append(0)

    out_arr = msg_dat + general_instr_byarr
    ser.write(out_arr)



def test_matrix_hsv():
    # Address and port for our esp32. if we are using sockets.
    server_address_port = ('192.168.1.27', 4040)
    matrix = udp_matrix.LEDMatrix(server_address_port, 64, 32)
    while True:
        for h in range(255):
            for y in range(32):
                for x in range(64):
                    hue_val = ((y * x)*6 + h * 3) % 255
                    matrix.set_led_hsv(x, y, hue_val, 255, 60)
            matrix.update()
            time.sleep(0.01)

def test_matrix_pyaudio():
    # Address and port for our esp32. if we are using sockets.
    server_address_port = ('192.168.1.27', 4040)
    matrix = udp_matrix.LEDMatrix(server_address_port, 64, 32)

    fft_handler = fft.MatrixFFT(64, 1100)
    fft_handler.begin()

    sound_arr = [0] * 64
    interval = 0
    decrement_val = 1

    while(1):
        fft_handler.capture_audio()
        fft_handler.proccess_fft()

        for i in range(64):
            if sound_arr[i] < 0:
                sound_arr[i] = 0

            if sound_arr[i] >= 24:
                sound_arr[i] = sound_arr[i] - 3 * decrement_val

            if sound_arr[i] < 24 and sound_arr[i] > 11:
                sound_arr[i] = sound_arr[i] - 2 * decrement_val

            else:
                sound_arr[i] = sound_arr[i] - 1 * decrement_val

        for x in range(64):
            intensity = 0
            if x == 0:
                intensity = int(fft_handler.data[1] / 100)
            else:
                intensity = int(fft_handler.data[x] / 100)

            if intensity > 31:
                intensity = 31

            if sound_arr[x] < intensity:
                sound_arr[x] = intensity

            for y in range(sound_arr[x]):
                matrix.set_led(x, 31 - y, sound_arr[x] * 8, 255 - sound_arr[x] * 8, 0)

            for y in range(31 - sound_arr[x]):
                if sound_arr[x] < 0:
                    sound_arr[x] = 0
                matrix.set_led(x, y, sound_arr[x] * 2, sound_arr[x] * 2, sound_arr[x] * 2)

            matrix.update()

#test_matrix_pyaudio()
#test_matrix_hsv()

test_status_serial()