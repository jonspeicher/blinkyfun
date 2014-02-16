import serial

class BlinkyTape(object):
    def __init__(self, port, baud_rate = 115200, pixel_count = 60):
        self._serial = serial.Serial(port, baud_rate)
        self._pixel_count = pixel_count

    @property
    def pixel_count(self):
        return self._pixel_count

    def update(self, pixels):
        UPDATE_VALUE = [0, 0, 255]
        for pixel in pixels:
            self._serial.write(pixel.raw)
        self._serial.write(UPDATE_VALUE)
        self._serial.flush()
        self._serial.flushInput()
