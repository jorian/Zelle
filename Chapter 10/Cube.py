__author__ = 'Jorian'

class Cube:
    def __init__(self, length):
        self.length = length

    def surfaceArea(self):
        return 6 * (self.length * self.length)

    def volumeCube(self):
        return self.length**3

