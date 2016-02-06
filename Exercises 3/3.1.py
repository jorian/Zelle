__author__ = 'Jorian'
# Calculate the volume and surface area given the radius = r
# V = 4/3 * pi * r ** 3
# A = 4 * pi * r ** 2
import math
def main():
    r = float(input("What is the radius: "))
    V = (4/3 * math.pi) * r ** 3
    A = (4 * math.pi) * r ** 2
    print("The volume is ", V,"m3 and the area is ", A,"m2.")

main()