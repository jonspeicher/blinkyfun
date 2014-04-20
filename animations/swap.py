from blinkytape import animation
import random

class Swap(animation.Animation):
    def __init__(self, pattern, frame_period_sec):
        super(Swap, self).__init__(frame_period_sec)
        self._pixels = pattern.pixels

    @property
    def finished(self):
        return not self._index_pairs

    def begin(self):
        indexes = range(0, len(self._pixels))
        random.shuffle(indexes)
        self._index_pairs = self._pairwise(indexes)

    def next_frame(self):
        first, second = self._index_pairs.pop()
        self._swap(self._pixels, first, second)
        return self._pixels

    def _swap(self, indexable, first, second):
        indexable[first], indexable[second] = indexable[second], indexable[first]

    def _pairwise(self, iterable):
        range_by_twos = range(0, len(iterable), 2)
        return [(iterable[i], iterable[i + 1]) for i in range_by_twos]
