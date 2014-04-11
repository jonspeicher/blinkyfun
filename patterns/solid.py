class Solid(object):
    def __init__(self, pixel_count, color):
        self._pixels = [color] * pixel_count

    @property
    def pixels(self):
        return list(self._pixels)
