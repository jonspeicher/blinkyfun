import blinkycolor
import serial

class BlinkyTape(object):
    def __init__(self, port, baud_rate = 115200, pixel_count = 60):
        self._serial = serial.Serial(port, baud_rate)
        self._pixel_count = pixel_count
        self._pixels = [blinkycolor.BLACK] * self._pixel_count

    @property
    def pixel_count(self):
        return self._pixel_count

    def set_pixel(self, index, color):
        if index >= self._pixel_count: raise IndexError
        self._pixels[index] = color

    def set_pixels(self, pixels):
        if len(pixels) != self._pixel_count: raise ValueError
        self._pixels = pixels

    def update(self):
        UPDATE_VALUE = [255, 255, 255]
        for pixel in self._pixels:
            self._serial.write(pixel.raw)
        self._serial.write(UPDATE_VALUE)
        self._serial.flush()
