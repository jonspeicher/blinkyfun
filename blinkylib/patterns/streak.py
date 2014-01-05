import blinkypattern
from blinkylib import blinkycolor

class Streak(blinkypattern.BlinkyPattern):
    # TBD: This is getting a little long; is there a better way? Properties?
    def __init__(self, blinkytape, color, pixel_count = 20, period_sec = 1):
        super(Streak, self).__init__(blinkytape)
        self._animated = True
        self._timebase_sec = period_sec / float(self._blinkytape.pixel_count)
        self._pixels = self._make_streak(color, pixel_count)

    def animate(self):
        self._blinkytape.set_pixels(self._pixels)
        self._blinkytape.update()
        self._pixels = self._pixels[1:] + [self._pixels[0]]

    def _make_streak(self, color, pixel_count):
        gradient = self._make_gradient(color, pixel_count)
        pad_pixel_count = self._blinkytape.pixel_count - pixel_count
        pad_pixels = [blinkycolor.BLACK] * pad_pixel_count
        return gradient + pad_pixels

    # TBD: This approach may not work for arbitrary fades as the scale steps
    # when changing between, say, red and green won't be uniform for all colors.
    def _make_gradient(self, color, step_count):
        final_intensity = 0.1
        scale_per_step = (1 - final_intensity) / (step_count - 1)
        scales = [1 - (scale_per_step * step) for step in range(0, step_count)]
        return [blinkycolor.BlinkyColor.scale(color, scale) for scale in scales]
