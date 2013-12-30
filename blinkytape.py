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
        self._pixels[index] = [min(color, 254) for color in rgb]

    def fill(self, rgb):
        for index in range(0, self._pixel_count):
            self.set_pixel(index, rgb)

    def update(self):
        pixels = self._pixels + [[255, 255, 255]]
        for pixel in pixels:
            self._serial.write(pixel)
        self._serial.flush()

bt = BlinkyTape('/dev/tty.usbmodem1411')
bt.fill(BlinkyTape.RED)
bt.update()

time.sleep(5)

bt.fill(BlinkyTape.GREEN)
bt.update()
