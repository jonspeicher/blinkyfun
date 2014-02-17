#!/usr/bin/env python

from blinkytape import blinkytape, blinkycolor, blinkyplayer
from patterns import gradient
import sys

tape = blinkytape.BlinkyTape.find_first()

start_color = blinkycolor.BlinkyColor.from_string(sys.argv[1])
end_color = blinkycolor.BlinkyColor.from_string(sys.argv[2])
pattern = gradient.Gradient(tape.pixel_count, start_color, end_color)

player = blinkyplayer.BlinkyPlayer(tape)
player.display_pattern(pattern)
