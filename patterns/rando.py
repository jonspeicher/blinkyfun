from blinkytape import blinkycolor

class Rando(object):
    def __init__(self, pixel_count):
        self._pixels = [blinkycolor.BlinkyColor.random() for i in range(pixel_count)]

    @property
    def pixels(self):
        return list(self._pixels)
