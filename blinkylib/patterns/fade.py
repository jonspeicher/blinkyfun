import blinkypattern
import itertools

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
        steps_per_period = int(period_sec / self._timebase_sec)
        circular_color_list = color_list + [color_list[0]]
        profile = []
        for this_color, next_color in self._pairwise(circular_color_list):
            ramp = self._make_color_ramp(this_color, next_color, steps_per_period)
            constant = self._make_constant_color(next_color, steps_per_period)
            profile.extend(ramp + constant)
        return profile

    def _make_constant_color(self, color, count):
        return [color] * count

    def _make_color_ramp(self, first_color, second_color, step_count):
        return []

    def _pairwise(self, iterable):
        this_iter, next_iter = itertools.tee(iterable)
        next(next_iter)
        return itertools.izip(this_iter, next_iter)
