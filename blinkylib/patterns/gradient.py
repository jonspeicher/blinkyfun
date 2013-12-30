import blinkypattern
import blinkylib.blinkycolor

class Gradient(blinkypattern.BlinkyPattern):
    def __init__(self, blinkytape, start_color, end_color):
        super(Gradient, self).__init__(blinkytape)
        self._start_color = start_color
        self._end_color = end_color

    def setup(self):
        super(Gradient, self).setup()
        pixels = self._make_rgb_gradient(self._start_color, self._end_color)
        self._blinkytape.set_pixels(pixels)
        self._blinkytape.update()

    def _make_rgb_gradient(self, start_color, end_color):
        pixel_count = self._blinkytape.pixel_count
        red_delta = self._make_delta(start_color.red, end_color.red, pixel_count)
        green_delta = self._make_delta(start_color.green, end_color.green, pixel_count)
        blue_delta = self._make_delta(start_color.blue, end_color.blue, pixel_count)
        pixels = []
        for index in range(0, pixel_count):
            red = start_color.red + (red_delta * index)
            green = start_color.green + (green_delta * index)
            blue = start_color.blue + (blue_delta * index)
            pixels.append(blinkylib.blinkycolor.BlinkyColor(red, green, blue))
        return pixels

    def _make_delta(self, start, end, step):
        return (end - start) / float(step)
