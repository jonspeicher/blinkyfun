import serial
import time

class BlinkyTape(object):
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    ORANGE = [255, 165, 0]
    YELLOW = [255, 255, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    PURPLE = [255, 0, 255]
    WHITE = [255, 255, 255]

    def __init__(self, port, pixel_count = 60):
        self._serial = serial.Serial(port, 57600)
        self._pixel_count = pixel_count
        self._pixels = [self.BLACK] * self._pixel_count

    def set_pixel(self, index, rgb):
        if index >= self._pixel_count: raise IndexError
        self._pixels[index] = [int(round(min(color, 254))) for color in rgb]

    def fill(self, rgb):
        for index in range(0, self._pixel_count):
            self.set_pixel(index, rgb)

    def gradient(self, start_rgb, end_rgb):
        start_rgb = [float(color) for color in start_rgb]
        end_rgb = [float(color) for color in end_rgb]
        red_delta = (end_rgb[0] - start_rgb[0]) / self._pixel_count
        green_delta = (end_rgb[1] - start_rgb[1]) / self._pixel_count
        blue_delta = (end_rgb[2] - start_rgb[2]) / self._pixel_count
        for index in range(0, self._pixel_count):
            red = start_rgb[0] + (red_delta * index)
            green = start_rgb[1] + (green_delta * index)
            blue = start_rgb[2] + (blue_delta * index)
            self.set_pixel(index, [red, green, blue])

    def update(self):
        pixels = self._pixels + [[255, 255, 255]]
        for pixel in pixels:
            self._serial.write(pixel)
        self._serial.flush()

bt = BlinkyTape('/dev/tty.usbmodem1411')
bt.gradient(BlinkyTape.RED, BlinkyTape.PURPLE)
bt.update()
