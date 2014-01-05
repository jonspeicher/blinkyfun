class BlinkyColor(object):
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    @classmethod
    def scale(cls, color, scale):
        return cls(color.red * scale, color.green * scale, color.blue * scale)

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    @property
    def raw(self):
        rgb = [self._red, self._green, self._blue]
        clipped_rgb = [min(color, 254) for color in rgb]
        rounded_rgb = [round(color) for color in clipped_rgb]
        truncated_rgb = [int(color) for color in rounded_rgb]
        return truncated_rgb

    def __repr__(self):
        return str(self.raw)

BLACK = BlinkyColor(0, 0, 0)
RED = BlinkyColor(255, 0, 0)
ORANGE = BlinkyColor(255, 165, 0)
YELLOW = BlinkyColor(255, 255, 0)
GREEN = BlinkyColor(0, 255, 0)
BLUE = BlinkyColor(0, 0, 255)
PURPLE = BlinkyColor(255, 0, 255)
WHITE = BlinkyColor(255, 255, 255)
