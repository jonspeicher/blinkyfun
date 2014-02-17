#!/usr/bin/env python

from blinkylib import blinkytape, blinkycolor
from blinkylib.patterns import gradient
import time

bt = blinkytape.BlinkyTape('/dev/tty.usbmodem1411')
pattern = gradient.Gradient(bt, blinkycolor.RED, blinkycolor.BLACK)
pattern.setup()

while pattern.animated:
    pattern.animate()
    time.sleep(pattern.timebase_sec)
