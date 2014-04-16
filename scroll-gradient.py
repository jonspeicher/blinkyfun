#!/usr/bin/env python

from blinkytape import tape, color, player
from patterns import gradient
from animations import scroll
import sys

tape = tape.BlinkyTape.find_first()

start_color = color.Color.from_string(sys.argv[1])
end_color = color.Color.from_string(sys.argv[2])
pattern = gradient.Gradient(tape.pixel_count, start_color, end_color)

frame_period_sec = float(sys.argv[3])
animation = scroll.Scroll(pattern, frame_period_sec)

player = player.Player(tape)
player.play_animation(animation, player.FOREVER)
