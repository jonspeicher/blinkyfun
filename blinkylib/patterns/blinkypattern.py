# TBD: patterns seem to use setup or animate but not both, nobody uses teardown
# yet; is it best not to call blinkytape methods? is it best to just have
# getpixels? is it best to have init always do static init and animate always
# do animate even for static patterns? gitpixels would have fewer dependencies
# e.g. it would not depend on blinkytape, and the performance benefit of knowing
# when and how ot call update and set pixels etc may not matter

class BlinkyPattern(object):
    def __init__(self, blinkytape):
        self._blinkytape = blinkytape
        self._animated = False
        self._timebase_sec = 0.01

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
