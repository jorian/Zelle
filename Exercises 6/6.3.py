__author__ = 'Jorian'
# Calculate the volume and surface area given the radius = r
# V = 4/3 * pi * r ** 3
# A = 4 * pi * r ** 2
import math

def sphereVolume(radius):
    volume = 4/3*math.pi*(radius**3)
    return volume

def sphereArea(radius):
    area = 4*math.pi*(radius**2)
    return area

def main():
    r = float(input("What is the radius: "))
    print("The volume is", sphereVolume(r),"m3 and the area is ", sphereArea(r),"m2.")

main()
