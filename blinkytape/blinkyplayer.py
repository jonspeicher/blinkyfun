import time

class BlinkyPlayer(object):
    FOREVER = -1

    def __init__(self, blinkytape):
        self._blinkytape = blinkytape

    def display_pattern(self, pattern):
        self._blinkytape.update(pattern.pixels)

    def play_animation(self, animation, num_cycles = FOREVER):
        player_finished = self._player_finished_predicate(num_cycles)
        while not player_finished():
            _play_single_animation_cycle(animation)

    def _play_single_animation_cycle(self, animation):
        animation.begin()
        while not animation.finished:
            pixels = animation.next_frame()
            self._blinkytape.update(pixels)
            time.sleep(animation.frame_period_sec)
        animation.end()

    def _player_finished_predicate(self, num_cycles):
        if num_cycles < 0 and num_cycles != self.FOREVER: raise ValueError
        if num_cycles == self.FOREVER:
            predicate = self._forever_predicate()
        else:
            predicate = self._cycle_count_predicate(num_cycles)
        return predicate

    def _forever_predicate(self):
        return lambda: False

    def _cycle_count_predicate(self, num_cycles):
        # Blah, Python 2.x can't modify a closed-over value (see nonlocal)
        self._num_cycles = num_cycles
        def predicate():
            finished = self._num_cycles <= 0
            self._num_cycles = self._num_cycles - 1
            return finished
        return predicate
