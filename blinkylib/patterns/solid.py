import blinkypattern

class Solid(blinkypattern.BlinkyPattern):
    def __init__(self, blinkytape, solid_color):
        super(Solid, self).__init__(blinkytape)
        self._pixels = [solid_color] * self._blinkytape.pixel_count

    def setup(self):
        super(Solid, self).setup()
        self._blinkytape.set_pixels(self._pixels)
        self._blinkytape.update()
