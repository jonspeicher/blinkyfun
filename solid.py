#!/usr/bin/env python

from blinkytape import tape, color, player
from patterns import solid
import sys

tape = tape.BlinkyTape.find_first()

color = color.Color.from_string(sys.argv[1])
pattern = solid.Solid(tape.pixel_count, color)

player = player.Player(tape)
player.display_pattern(pattern)
