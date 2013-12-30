import serial

class BlinkyTape(object):
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    ORANGE = [255, 165, 0]
    YELLOW = [255, 255, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    PURPLE = [255, 0, 255]
    WHITE = [255, 255, 255]

    def __init__(self, port, pixel_count = 60):
        self._serial = serial.Serial(port, 57600)
        self._pixel_count = pixel_count
        self._pixels = [self.BLACK] * self._pixel_count

    @property
    def pixel_count(self):
        return self._pixel_count

    def set_pixel(self, index, rgb):
        if index >= self._pixel_count: raise IndexError
        clipped_rgb = [min(color, 254) for color in rgb]
        rounded_rgb = [round(color) for color in clipped_rgb]
        truncated_rgb = [int(color) for color in rounded_rgb]
        self._pixels[index] = truncated_rgb

    def set_pixels(self, pixels):
        if len(pixels) != self._pixel_count: raise ValueError
        for index in range(0, self._pixel_count):
            self.set_pixel(index, pixels[index])

    def update(self):
        UPDATE_VALUE = [255, 255, 255]
        pixels = self._pixels + [UPDATE_VALUE]
        for pixel in pixels:
            self._serial.write(pixel)
        self._serial.flush()
