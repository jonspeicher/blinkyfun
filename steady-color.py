#!/usr/bin/env python

from blinkytape import blinkytape, blinkycolor, blinkyplayer
from patterns import solid
import sys

address = blinkytape.BlinkyTape.find_first()
tape = blinkytape.BlinkyTape(address)
color = blinkycolor.BlinkyColor.from_string(sys.argv[1])
pattern = solid.Solid(tape, color)
player = blinkyplayer.BlinkyPlayer(tape)
player.display_pattern(pattern)
