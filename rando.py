#!/usr/bin/env python

from blinkytape import blinkytape, blinkyplayer
from patterns import rando

tape = blinkytape.BlinkyTape.find_first()
pattern = rando.Rando(tape.pixel_count)

player = blinkyplayer.BlinkyPlayer(tape)
player.display_pattern(pattern)
