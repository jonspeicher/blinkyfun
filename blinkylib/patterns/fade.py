import blinkypattern
import blinkylib.blinkycolor
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
            ramp = self._make_rgb_ramp(this_color, next_color, steps_per_period)
            constant = [next_color] * steps_per_period
            profile.extend(ramp + constant)
        return profile

    def _make_rgb_ramp(self, start_color, end_color, step_count):
        red_ramp = self._make_ramp(start_color.red, end_color.red, step_count)
        green_ramp = self._make_ramp(start_color.green, end_color.green, step_count)
        blue_ramp = self._make_ramp(start_color.blue, end_color.blue, step_count)
        rgb_ramp = zip(red_ramp, green_ramp, blue_ramp)
        return [blinkylib.blinkycolor.BlinkyColor(*rgb) for rgb in rgb_ramp]

    def _make_ramp(self, start, end, count):
        delta = (end - start) / float(count)
        return [start + (delta * index) for index in range(0, count)]

    def _pairwise(self, iterable):
        this_iter, next_iter = itertools.tee(iterable)
        next(next_iter)
        return itertools.izip(this_iter, next_iter)
