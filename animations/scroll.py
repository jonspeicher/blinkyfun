from blinkytape import animation

class Scroll(animation.Animation):
    def __init__(self, pattern, frame_period_sec):
        super(Scroll, self).__init__(frame_period_sec)
        self._pattern = pattern

    @property
    def finished(self):
        return self._offset == len(self._pattern.pixels)

    def begin(self):
        self._offset = -1

    def next_frame(self):
        self._offset = self._offset + 1
        if self._offset > len(self._pattern.pixels): raise RuntimeError
        pixels = self._pattern.pixels
        return pixels[self._offset:] + pixels[:self._offset]
