#!/usr/bin/env python

from blinkytape import tape, color, player
from patterns import gradient
import sys

tape = tape.BlinkyTape.find_first()

start_color = color.Color.from_string(sys.argv[1])
end_color = color.Color.from_string(sys.argv[2])
pattern = gradient.Gradient(tape.pixel_count, start_color, end_color)

player = player.Player(tape)
player.display_pattern(pattern)
