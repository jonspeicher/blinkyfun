class Solid(object):
    def __init__(self, config, color):
        self._pixels = [color] * config.pixel_count

    @property
    def pixels(self):
        return self._pixels
