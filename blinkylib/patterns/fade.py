import blinkypattern

# TBD: TrapezoidalFade vs SinusoidalFade?
class Fade(blinkypattern.BlinkyPattern):
    def __init__(self, blinkytape, color_list, period_sec):
        super(Fade, self).__init__(blinkytape)
        self._animated = True
        self._index = 0
        self._profile = self._make_fade_profile(color_list, period_sec)

    def animate(self):
        super(Fade, self).setup()
        pixels = [self._profile[self._index]] * self._blinkytape.pixel_count
        self._blinkytape.set_pixels(pixels)
        self._blinkytape.update()
        self._index = (self._index + 1) % len(self._profile)

    def _make_fade_profile(self, color_list, period_sec):
        steps_per_period = period_sec / self._timebase_sec
        profile = []
        for color in color_list:
            profile.extend([color] * int(steps_per_period))
        return profile
