__author__ = 'Jorian'
import math

def main():
    a, b, c = eval(input("Geef de coefficienten svp: "))

    discRoot = math.sqrt((b * b) - 4 * a * c) #sommige uitkomsten zijn niet mogelijk
    root1 = (-b + discRoot) / (2 * a)
    root2 = (+b + discRoot) / (2 * a)

    print()
    print("De oplossingen zijn:", root1, root2)
main()