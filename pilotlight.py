#!/usr/bin/env python

from blinkylib import blinkytape, blinkycolor
from blinkylib.patterns import gradient

bt = blinkytape.BlinkyTape('/dev/tty.usbmodem1421')
pattern = gradient.Gradient(bt, blinkycolor.BLUE, blinkycolor.WHITE)
pattern.setup()
