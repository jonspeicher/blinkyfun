#!/usr/bin/env python

import gradient
from blinkytape import BlinkyTape

bt = BlinkyTape('/dev/tty.usbmodem1421')
view = gradient.Gradient(bt, BlinkyTape.BLUE, BlinkyTape.WHITE)
view.setup()
