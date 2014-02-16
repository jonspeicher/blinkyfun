import blinkyanimation

class Steady(blinkyanimation.BlinkyAnimation):
    def __init__(self, pattern):
        super(Steady, self).__init__(frame_count = 1, frame_period_sec = 0.1)
        self._pattern = pattern

    def next_frame(self):
        return self._pattern.pixels
