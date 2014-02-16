import time

class BlinkyPlayer(object):
    FOREVER = -1

    def __init__(self, blinkytape):
        self._blinkytape = blinkytape

    def play(self, animation, num_cycles = FOREVER):
        finished = self._finished_predicate(animation, num_cycles)
        animation.begin()
        while not finished():
            pixels = animation.next_frame()
            self._blinkytape.update(pixels)
            time.sleep(animation.frame_period_sec)
        animation.end()

    def _finished_predicate(self, animation, num_cycles):
        if num_cycles < 0 and num_cycles != self.FOREVER: raise ValueError
        if num_cycles == self.FOREVER:
            predicate = self._forever_predicate()
        else:
            self._num_frames = animation.frame_count * num_cycles
            predicate = self._frame_count_predicate()
        return predicate

    def _forever_predicate(self):
        return lambda: False

    def _frame_count_predicate(self):
        def predicate():
            finished = self._num_frames <= 0
            self._num_frames = self._num_frames - 1
            return finished
        return predicate
