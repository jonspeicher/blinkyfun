class BlinkyPattern(object):
    def __init__(self, blinkytape):
        self._blinkytape = blinkytape
        self._animated = False
        self._timebase_sec = 0.1

    @property
    def animated(self):
        return self._animated

    @property
    def timebase_sec(self):
        return self._timebase_sec

    def setup(self):
        pass

    def animate(self):
        pass

    def teardown(self):
        pass
