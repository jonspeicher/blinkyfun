#!/usr/bin/env python

from blinkytape import tape, player
from patterns import random
from animations import swap
import sys

tape = tape.BlinkyTape.find_first()

pattern = random.Random(tape.pixel_count)

frame_period_sec = float(sys.argv[1])
animation = swap.Swap(pattern, frame_period_sec)

player = player.Player(tape)
player.play_animation(animation, player.FOREVER)
