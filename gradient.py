import blinkyview

class Gradient(blinkyview.BlinkyView):
    def __init__(self, blinkytape, start_rgb, end_rgb):
        super(Gradient, self).__init__(blinkytape)
        self._start_rgb = self._floatify(start_rgb)
        self._end_rgb = self._floatify(end_rgb)

    def setup(self):
        super(Gradient, self).setup()
        pixels = self._make_rgb_gradient(self._start_rgb, self._end_rgb)
        self._blinkytape.set_pixels(pixels)
        self._blinkytape.update()

    def _make_rgb_gradient(self, start_rgb, end_rgb):
        pixel_count = self._blinkytape.pixel_count
        red_delta = self._make_delta(start_rgb[0], end_rgb[0], pixel_count)
        green_delta = self._make_delta(start_rgb[1], end_rgb[1], pixel_count)
        blue_delta = self._make_delta(start_rgb[2], end_rgb[2], pixel_count)
        pixels = []
        for index in range(0, pixel_count):
            red = start_rgb[0] + (red_delta * index)
            green = start_rgb[1] + (green_delta * index)
            blue = start_rgb[2] + (blue_delta * index)
            pixels.append([red, green, blue])
        return pixels

    def _floatify(self, iterable):
        return [float(item) for item in iterable]

    def _make_delta(self, start, end, step):
        return (end - start) / step
