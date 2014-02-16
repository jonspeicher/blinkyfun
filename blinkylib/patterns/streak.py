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
    # It should work for computing a 0.1-scaled final intensity that could then
    # be passed into a gradient to make the pattern for the streak animation,
    # though, e.g.
    # pattern = Gradient(BlinkyColor.YELLOW, BlinkyColor.scale(BlinkyColor.YELLOW, 0.1), 20)
    # animation = Streak(pattern, 1)
    # TBD: What did I want scale for? Just this case? (I think so, I think I
    # dreamed it, mostly, I was dreaming color increment and decrement); Also,
    # what is meaningful about >1 scale? I think nothing?
    # TBD: Also, will the pattern/transition architecture work with the
    # stock firmware pattern that does the three-phase thing? Or is there
    # a way to make it do so? Maybe some transitions/animations could
    # be initialized with patterns like fade and static and streak and
    # some might be standalone, like the rainbow three-phase thing? Or
    # consider just random pixels in random colors as fast as possible?
    # That wouldn't require a fixed pattern, but could still fit the
    # "animation" interface.
    # What about sinusoidal fade? If trap fade is fade between lists of
    # continuous patterns, wouldn't sin fade be the same thing? But, now
    # that I think of it, does trap fade work for noncontinuous patterns?
    # I think it does; it just works on a per-pixel basis instead of a
    # per-strip basis
    def _make_gradient(self, color, step_count):
        final_intensity = 0.1
        scale_per_step = (1 - final_intensity) / (step_count - 1)
        scales = [1 - (scale_per_step * step) for step in range(0, step_count)]
        return [blinkycolor.BlinkyColor.scale(color, scale) for scale in scales]
