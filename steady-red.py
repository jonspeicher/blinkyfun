#!/usr/bin/env python

from blinkytape import blinkytape, blinkycolor, blinkyplayer
from patterns import solid
from animations import steady
import sys

tape = blinkytape.BlinkyTape(sys.argv[1])
pattern = solid.Solid(tape, blinkycolor.RED)
animation = steady.Steady(pattern)
player = blinkyplayer.BlinkyPlayer(tape)
player.play(animation, num_cycles = 1)
