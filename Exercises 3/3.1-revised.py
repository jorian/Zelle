__author__ = 'Jorian'
# Calculate the volume and surface area given the radius = r
# V = 4/3 * pi * r ** 3
# A = 4 * pi * r ** 2
from GeoSphere import *
from Cube import *


def main():
    r = float(input("What is the radius: "))
    sphere = GeoSphere(r)

    print("The volume is {0:0.0f} m3 and the area is {1:0.0f} m2.".format(sphere.volume(),sphere.surfaceArea()))

    l = float(input("What is the length of a side?"))
    cube = Cube(l)

    print("The volume is {0:0.0f} m3 and the area is {1:0.0f} m2.".format(cube.volumeCube(),cube.surfaceArea()))
main()