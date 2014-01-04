#!/usr/bin/env python

from blinkylib import blinkytape, blinkycolor
from blinkylib.patterns import streak
import time

bt = blinkytape.BlinkyTape('/dev/tty.usbmodem1421')
pattern = streak.Streak(bt, blinkycolor.ORANGE, 20)
pattern.setup()

while pattern.animated:
    pattern.animate()
    time.sleep(pattern.timebase_sec)
