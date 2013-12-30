#!/usr/bin/env python

from blinkylib.blinkytape import BlinkyTape
from blinkylib.patterns.gradient import Gradient
from blinkylib import blinkycolor

bt = BlinkyTape('/dev/tty.usbmodem1421')
pattern = Gradient(bt, blinkycolor.BLUE, blinkycolor.WHITE)
pattern.setup()
