import blinkypattern
# TBD: from import?
import blinkylib.blinkycolor

class Streak(blinkypattern.BlinkyPattern):
    # TBD: This is getting a little long; is there a better way? Properties?
    def __init__(self, blinkytape, color, pixel_count = 20, period_sec = 1):
        super(Streak, self).__init__(blinkytape)
        self._animated = True
        # TBD use period to adjust timebase?
        self._pixels = self._make_streak(color, pixel_count)

    def animate(self):
        self._blinkytape.set_pixels(self._pixels)
        self._blinkytape.update()
        self._pixels = self._pixels[1:] + [self._pixels[0]]

    def _make_streak(self, color, pixel_count):
        gradient = self._make_gradient(color, pixel_count)
        pad_pixel_count = self._blinkytape.pixel_count - pixel_count
        pad_pixels = [blinkylib.blinkycolor.BLACK] * pad_pixel_count
        return gradient + pad_pixels

    def _make_gradient(self, color, pixel_count):
        final_intensity = 0.1
        percent_reduction_per_step = (1 - final_intensity) / (pixel_count - 1)
        gradient = []
        for index in range(0, pixel_count):
            scale = 1 - (percent_reduction_per_step * index)
            red = color.red * scale
            green = color.green * scale
            blue = color.blue * scale
            gradient.append(blinkylib.blinkycolor.BlinkyColor(red, green, blue))
        return gradient
