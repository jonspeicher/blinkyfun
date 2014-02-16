import time

class BlinkyPlayer(object):
    FOREVER = -1

    def __init__(self, blinkytape):
        self._blinkytape = blinkytape

    def play(self, animation, num_cycles = FOREVER):
        finished = self._make_finished_predicate(animation, num_cycles)
        animation.begin()
        while not finished():
            pixels = animation.next_frame()
            self._blinkytape.update(pixels)
            time.sleep(animation.frame_period_sec)
        animation.end()

    def _make_finished_predicate(self, animation, num_cycles):
        if num_cycles < 0 and num_cycles != self.FOREVER: raise ValueError
        if num_cycles == self.FOREVER:
            predicate = lambda: False
        else:
            self._num_frames = animation.frame_count * num_cycles
            def predicate():
                finished = self._num_frames <= 0
                self._num_frames = self._num_frames - 1
                return finished
        return predicate
