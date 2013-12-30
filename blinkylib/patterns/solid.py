import blinkypattern

class Solid(blinkypattern.BlinkyPattern):
    def __init__(self, blinkytape, solid_rgb):
        super(Solid, self).__init__(blinkytape)
        self._solid_rgb = solid_rgb

    def setup(self):
        super(Solid, self).setup()
        pixels = [self._solid_rgb] * self._blinkytape.pixel_count
        self._blinkytape.set_pixels(pixels)
        self._blinkytape.update()
