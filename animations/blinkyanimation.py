# TBD: Some animations mutate a pattern: shift it, fade it, etc.
# Not all animations need a pattern
# I need a rainbow pattern for fun

class BlinkyAnimation(object):
    def __init__(self, frame_count, frame_period_sec):
        if frame_count < 0 or frame_period_sec < 0: raise ValueError
        self._frame_count = frame_count
        self._frame_period_sec = frame_period_sec

    @property
    def frame_count(self):
        return self._frame_count

    @property
    def frame_period_sec(self):
        return self._frame_period_sec

    def begin(self):
        pass

    def next_frame(self):
        pass

    def end(self):
        pass
