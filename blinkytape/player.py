import time

class Player(object):
    FOREVER = -1

    def __init__(self, blinkytape):
        self._blinkytape = blinkytape

    def display_pattern(self, pattern):
        self._blinkytape.update(pattern.pixels)

    def play_animation(self, animation, num_cycles):
        while num_cycles == self.FOREVER or num_cycles > 0:
            self._play_single_animation_cycle(animation)
            if num_cycles != self.FOREVER:
                num_cycles = num_cycles - 1

    def _play_single_animation_cycle(self, animation):
        animation.begin()
        while not animation.finished:
            pixels = animation.next_frame()
            self._blinkytape.update(pixels)
            time.sleep(animation.frame_period_sec)
        animation.end()
