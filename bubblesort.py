#!/usr/bin/env python

# TBD: Sort animation could take a pattern that it assumed to be "final",
# shuffle it, then take a sort generator that produced a step in the sort
# algorithm at every call. It would be sorting shuffled indices that the
# animation would use to construct each frame.

from blinkytape import blinkytape, blinkycolor, blinkyplayer
from patterns import gradient
import random, sys, time

tape = blinkytape.BlinkyTape.find_first()

start_color = blinkycolor.BlinkyColor.from_string(sys.argv[1])
end_color = blinkycolor.BlinkyColor.from_string(sys.argv[2])
pattern = gradient.Gradient(tape.pixel_count, start_color, end_color)

indexes = range(0, tape.pixel_count)
random.shuffle(indexes)
pixels = [pattern.pixels[index] for index in indexes]
tape.update(pixels)

time.sleep(5)

swap_occurred = True
while swap_occurred:
    swap_occurred = False
    for i in range(1, tape.pixel_count):
        if indexes[i - 1] > indexes[i]:
            temp = indexes[i - 1]
            indexes[i - 1] = indexes[i]
            indexes[i] = temp
            swap_occurred = True
            pixels = [pattern.pixels[index] for index in indexes]
            tape.update(pixels)
