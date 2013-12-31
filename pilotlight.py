#!/usr/bin/env python

from blinkylib import blinkytape, blinkycolor
from blinkylib.patterns import fade
import time

bt = blinkytape.BlinkyTape('/dev/tty.usbmodem1421')
color_list = [blinkycolor.BLACK, blinkycolor.BLUE, blinkycolor.WHITE]
pattern = fade.Fade(bt, color_list, 1)
pattern.setup()

while pattern.animated:
    pattern.animate()
    time.sleep(pattern.timebase_sec)
