#!/usr/bin/env python

from blinkytape import BlinkyTape

bt = BlinkyTape('/dev/tty.usbmodem1411')
bt.gradient(BlinkyTape.BLUE, BlinkyTape.WHITE)
bt.update()
