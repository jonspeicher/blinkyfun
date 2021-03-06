# TBD: Some animations mutate a pattern: shift it, fade it, etc.
# Not all animations need a pattern
# I need a rainbow pattern for fun

# TBD: How do you do random pixels? is it a pattern that is permuted by the
# animation? YES; patterns are static, animations do things with patterns,
# rotate them, scramble them, scale them, sort them, etcetera

class Animation(object):
    def __init__(self, frame_period_sec):
        if frame_period_sec < 0: raise ValueError
        self._frame_period_sec = frame_period_sec

    @property
    def frame_period_sec(self):
        return self._frame_period_sec

    @property
    def finished(self):
        raise NotImplementedError('Animation must implement finished property')

    def begin(self):
        pass

    def next_frame(self):
        raise NotImplementedError('Animation must implement next_frame method')

    def end(self):
        pass
