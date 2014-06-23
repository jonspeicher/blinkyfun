from blinkytape import color

class Random(object):
    def __init__(self, pixel_count):
        self._pixels = [color.Color.random() for i in range(pixel_count)]

    @property
    def pixels(self):
        return list(self._pixels)
