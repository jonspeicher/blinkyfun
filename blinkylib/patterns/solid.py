import blinkypattern

class Solid(blinkypattern.BlinkyPattern):
    def __init__(self, blinkytape, rgb):
        super(Solid, self).__init__(blinkytape)
        self._rgb = rgb

    def setup(self):
        super(Solid, self).setup()
        pixels = [self._rgb] * self._blinkytape.pixel_count
        self._blinkytape.set_pixels(pixels)
        self._blinkytape.update()
