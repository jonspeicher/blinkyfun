#!/usr/bin/env python

from blinkytape import blinkytape, blinkycolor, blinkyplayer
from patterns import solid
import sys

tape = blinkytape.BlinkyTape.find_first()

color = blinkycolor.BlinkyColor.from_string(sys.argv[1])
pattern = solid.Solid(tape.pixel_count, color)

player = blinkyplayer.BlinkyPlayer(tape)
player.display_pattern(pattern)
