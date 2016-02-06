__author__ = 'Jorian'
import math


def function():
    a, b, c = eval(input("Geef de coefficienten svp: "))

    discriminant = (b * b) - 4 * a * c
    if discriminant > 0:
        discRoot = math.sqrt(discriminant)  # sommige uitkomsten zijn niet mogelijk
        root1 = (-b + discRoot) / (2 * a)
        root2 = (+b + discRoot) / (2 * a)

        print()
        print("De oplossingen zijn:", root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("There is a double root at", root)
    else:
        print("Cannot take root from numbers less than zero!")


if __name__ == '__main__':
    function()
