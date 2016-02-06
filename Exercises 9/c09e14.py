__author__ = 'Jorian'


class RandomWalk:
    from graphics import *
    from random import random
    from math import pi, cos, sin

    def main():
        nSteps = getInput()
        steps(nSteps)

    def getInput():
        return int(input("How many steps from the center point? "))

    def steps(nSteps):
        win = GraphWin("Trace my walk", 1200, 1200)
        win.setCoords(-300, -300, 300, 300)
        x = y = 0
        curr = Point(x, y)
        next = Point(x, y)
        for i in range(nSteps):
            angle = random() * 2 * pi
            x = cos(angle)
            y = sin(angle)
            next.move(x, y)
            Line(curr, next).draw(win)
            curr.move(x, y)
        win.getMouse()

    def line(pOld, pNew):
        win = GraphWin("Trace my walk", 100, 100)
        line = Line(pOld, pNew)
        line.draw(win)
        win.getMouse()

    if __name__ == '__main__':
        main()
