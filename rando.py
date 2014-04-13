#!/usr/bin/env python

from blinkytape import tape, player
from patterns import rando

tape = tape.BlinkyTape.find_first()
pattern = rando.Rando(tape.pixel_count)

player = player.Player(tape)
player.display_pattern(pattern)
