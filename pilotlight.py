#!/usr/bin/env python

from patterns.gradient import Gradient
from blinkytape import BlinkyTape

bt = BlinkyTape('/dev/tty.usbmodem1421')
pattern = Gradient(bt, BlinkyTape.BLUE, BlinkyTape.WHITE)
pattern.setup()
