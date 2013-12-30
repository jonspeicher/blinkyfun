import blinkypattern
import blinkylib.blinkycolor

class Gradient(blinkypattern.BlinkyPattern):
    def __init__(self, blinkytape, start_color, end_color):
        super(Gradient, self).__init__(blinkytape)
        self._pixels = self._make_rgb_gradient(start_color, end_color)

    def setup(self):
        super(Gradient, self).setup()
        self._blinkytape.set_pixels(self._pixels)
        self._blinkytape.update()

    def _make_rgb_gradient(self, start_color, end_color):
        pixel_count = self._blinkytape.pixel_count
        red_gradient = self._make_gradient(start_color.red, end_color.red, pixel_count)
        green_gradient = self._make_gradient(start_color.green, end_color.green, pixel_count)
        blue_gradient = self._make_gradient(start_color.blue, end_color.blue, pixel_count)
        rgb_gradient = zip(red_gradient, green_gradient, blue_gradient)
        return [blinkylib.blinkycolor.BlinkyColor(*rgb) for rgb in rgb_gradient]

    def _make_gradient(self, start, end, count):
        delta = (end - start) / float(count)
        return [start + (delta * index) for index in range(0, count)]
