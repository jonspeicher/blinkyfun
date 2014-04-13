#!/usr/bin/env python

from blinkytape import blinkytape, blinkyanimation, blinkyplayer

class DummyTape(object):
    def update(self, pixels):
        pass

class TestAnimation(blinkyanimation.BlinkyAnimation):
    def __init__(self):
        super(TestAnimation, self).__init__(frame_period_sec = 1)

    @property
    def finished(self):
        return self._frames_remaining <= 0

    def begin(self):
        self._frames_remaining = 3

    def next_frame(self):
        self._frames_remaining = self._frames_remaining - 1
        print '   frames remaining: ' + str(self._frames_remaining)
        return []

tape = DummyTape()
animation = TestAnimation()
player = blinkyplayer.BlinkyPlayer(tape)

player.play_animation(animation, 5)
