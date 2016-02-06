__author__ = 'Jorian'

from random import random
from graphics import *
from math import *


def main():
    n = getInputs()
    h = simulate(n)
    pi = estimate(n, h)
    printOutput(pi)


def getInputs():
    return int(input("How many darts to throw? "))

def simulate(n):
    h = 0
    for i in range(n):
        point = Point(((2*random()) - 1), ((2*random()) - 1))
        print(point.getX(), point.getY())
        if (point.getX()**2) + (point.getY()**2) <= 1:
            h = h + 1
    return h


def estimate(n, h):
    pi = 4 * (h / n)
    return pi


def printOutput(pi):
    print("This is pi, according to algorithm:", pi)


if __name__ == '__main__':
    main()
