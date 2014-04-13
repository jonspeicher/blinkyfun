import random, sys

class Color(object):
    def __init__(self, red, green, blue):
        self._red = self._clamp_color(red)
        self._green = self._clamp_color(green)
        self._blue = self._clamp_color(blue)

    @classmethod
    def from_string(cls, string):
        return getattr(sys.modules[__name__], string.upper())

    @classmethod
    def random(cls):
        rgb = [random.randint(0, 255) for i in range(3)]
        return cls(*rgb)

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
    def rgb(self):
        return [self.red, self.green, self.blue]

    @property
    def raw(self):
        clipped_rgb = [min(color, 254.0) for color in self.rgb]
        rounded_rgb = [round(color) for color in clipped_rgb]
        truncated_rgb = [int(color) for color in rounded_rgb]
        return truncated_rgb

    def _clamp_color(self, color):
        return max(0.0, min(255.0, color))

    def __repr__(self):
        return str(self.rgb)

BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
ORANGE = Color(255, 165, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PURPLE = Color(255, 0, 255)
WHITE = Color(255, 255, 255)
