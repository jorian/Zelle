__author__ = 'Jorian'
import math
def main():
    height = float(input("Give the height of to where the ladder must reach:"))
    angle = float(input("Give the angle of the ladder in degrees:"))
    angleradians = angle * (math.pi / 180)
    length = height / math.sin(angleradians)
    print("The length of the ladder must be", length, "meters long.")
main()
