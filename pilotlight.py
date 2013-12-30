#!/usr/bin/env python

import gradient
from blinkytape import BlinkyTape

bt = BlinkyTape('/dev/tty.usbmodem1421')
pattern = gradient.Gradient(bt, BlinkyTape.BLUE, BlinkyTape.WHITE)
pattern.setup()
