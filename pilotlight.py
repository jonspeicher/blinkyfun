#!/usr/bin/env python

from blinkylib import blinkytape, blinkycolor
from blinkylib.patterns import fade
import time

bt = blinkytape.BlinkyTape('/dev/tty.usbmodem1411')
color_list = [blinkycolor.BLACK, blinkycolor.RED, blinkycolor.ORANGE,
        blinkycolor.YELLOW, blinkycolor.GREEN, blinkycolor.BLUE,
        blinkycolor.PURPLE, blinkycolor.WHITE]
pattern = fade.Fade(bt, color_list, 1)
pattern.setup()

while pattern.animated:
    pattern.animate()
    time.sleep(pattern.timebase_sec)
