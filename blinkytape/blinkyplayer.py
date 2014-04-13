import time

class BlinkyPlayer(object):
    FOREVER = -1

    def __init__(self, blinkytape):
        self._blinkytape = blinkytape

    def display_pattern(self, pattern):
        self._blinkytape.update(pattern.pixels)

    def play_animation(self, animation, num_cycles):
        # Loop for index in range(0,count)
        # Or for infinite generator
        # Or While num_cycles == infinite or num_cycles-- > 0
        cycles_finished = self._cycles_finished_predicate(num_cycles)
        while not cycles_finished():
            self._play_single_animation_cycle(animation)

    def _play_single_animation_cycle(self, animation):
        animation.begin()
        while not animation.finished:
            pixels = animation.next_frame()
            self._blinkytape.update(pixels)
            time.sleep(animation.frame_period_sec)
        animation.end()

    def _cycles_finished_predicate(self, num_cycles):
        if num_cycles < 0 and num_cycles != self.FOREVER: raise ValueError
        if num_cycles == self.FOREVER:
            predicate = self._never_finish()
        else:
            predicate = self._finish_after_countdown_from(num_cycles)
        return predicate

    def _never_finish(self):
        return lambda: False

    def _finish_after_countdown_from(self, num_cycles):
        cycles_remaining = [num_cycles]
        def predicate():
            finished = cycles_remaining[0] <= 0
            cycles_remaining[0] = cycles_remaining[0] - 1
            return finished
        return predicate
