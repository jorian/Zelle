__author__ = 'Jorian'

import math

class GeoSphere:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * (self.radius * self.radius)

    def volume(self):
        return (4/3) * math.pi * (self.radius**3)

