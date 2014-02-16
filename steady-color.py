#!/usr/bin/env python

from blinkytape import blinkytape, blinkycolor, blinkyplayer
from patterns import solid
from animations import steady
import sys

tape = blinkytape.BlinkyTape(sys.argv[1])
color = blinkycolor.BlinkyColor.from_string(sys.argv[2])
pattern = solid.Solid(tape, color)
animation = steady.Steady(pattern)
player = blinkyplayer.BlinkyPlayer(tape)
player.play(animation, num_cycles = 1)
