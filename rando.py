#!/usr/bin/env python

from blinkytape import tape, player
from patterns import random

tape = tape.BlinkyTape.find_first()

pattern = random.Random(tape.pixel_count)

player = player.Player(tape)
player.display_pattern(pattern)
