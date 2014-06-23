from blinkytape import animation, color
import random

class Swap(animation.Animation):
    def __init__(self, pattern, frame_period_sec):
        super(Swap, self).__init__(frame_period_sec)
        self._pixels = pattern.pixels

    @property
    def finished(self):
        # TBD: There is some weird off-by-one here; the last swap sequence won't finish
        # because the list goes empty after blanking the first pixel
        return not self._index_pairs

    def begin(self):
        indexes = range(0, len(self._pixels))
        random.shuffle(indexes)
        self._index_pairs = self._pairwise(indexes)
        self._swap_state_handler = self._swap_state_blank_first_pixel

    def next_frame(self):
        self._swap_state_handler()
        return self._pixels

    def _swap_state_blank_first_pixel(self):
        self._swap_pair = self._index_pairs.pop()
        self._temp_swap_pixel = self._pixels[self._swap_pair[0]]
        self._pixels[self._swap_pair[0]] = color.BLACK
        self._swap_state_handler = self._swap_state_place_swapped_second_pixel

    def _swap_state_place_swapped_second_pixel(self):
        self._pixels[self._swap_pair[0]] = self._pixels[self._swap_pair[1]]
        self._pixels[self._swap_pair[1]] = color.BLACK
        self._swap_state_handler = self._swap_state_place_swapped_first_pixel

    def _swap_state_place_swapped_first_pixel(self):
        self._pixels[self._swap_pair[1]] = self._temp_swap_pixel
        self._swap_state_handler = self._swap_state_blank_first_pixel

    def _pairwise(self, iterable):
        range_by_twos = range(0, len(iterable), 2)
        return [(iterable[i], iterable[i + 1]) for i in range_by_twos]
