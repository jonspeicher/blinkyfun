from blinkytape import blinkycolor

class Gradient(object):
    def __init__(self, pixel_count, start_color, end_color):
        self._pixels = self._rgb_gradient(pixel_count, start_color, end_color)

    @property
    def pixels(self):
        return self._pixels

    def _rgb_gradient(self, pixel_count, start_color, end_color):
        red_gradient = self._gradient(start_color.red, end_color.red, pixel_count)
        green_gradient = self._gradient(start_color.green, end_color.green, pixel_count)
        blue_gradient = self._gradient(start_color.blue, end_color.blue, pixel_count)
        rgb_gradient = zip(red_gradient, green_gradient, blue_gradient)
        return [blinkycolor.BlinkyColor(*rgb) for rgb in rgb_gradient]

    def _gradient(self, start, end, count):
        delta = (end - start) / float(count - 1)
        return [start + (delta * index) for index in range(0, count)]
