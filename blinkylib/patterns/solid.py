import blinkypattern

class Solid(blinkypattern.BlinkyPattern):
    def __init__(self, blinkytape, solid_color):
        super(Solid, self).__init__(blinkytape)
        self._solid_color = solid_color

    def setup(self):
        super(Solid, self).setup()
        pixels = [self._solid_color] * self._blinkytape.pixel_count
        self._blinkytape.set_pixels(pixels)
        self._blinkytape.update()
