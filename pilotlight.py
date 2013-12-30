#!/usr/bin/env python

from blinkylib.blinkytape import BlinkyTape
from blinkylib.patterns.gradient import Gradient

bt = BlinkyTape('/dev/tty.usbmodem1421')
pattern = Gradient(bt, BlinkyTape.BLUE, BlinkyTape.WHITE)
pattern.setup()
