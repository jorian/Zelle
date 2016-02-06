__author__ = 'Jorian'
from graphics import *

def ch42():
    win = GraphWin("Archer")
    win.setCoords(0,0,10,10)
    center = Point(5,5)

    circle1 = Circle(center, 5)
    circle1.setFill("white")
    circle1.setOutline("white")
    circle1.draw(win)

    circle2 = Circle(center, 4)
    circle2.setFill("black")
    circle2.setOutline("black")
    circle2.draw(win)

    circle3 = Circle(center, 3.0)
    circle3.setFill("blue")
    circle3.setOutline("blue")
    circle3.draw(win)

    circle4 = Circle(center, 2.0)
    circle4.setFill("red")
    circle4.setOutline("red")
    circle4.draw(win)

    circle5 = Circle(center, 1.0)
    circle5.setFill("yellow")
    circle5.setOutline("yellow")
    circle5.draw(win)

    points = 0
    for i in range(20):
        position = win.getMouse()
        positionX = round(position.getX())
        positionY = round(position.getY())
        print(positionY + positionX)

        #print(positionX, positionY)

        if positionX in (4, 5) and positionY in (4, 5):
            points = points + 5
        #elif position in

        print(points)

    win.getMouse()
    win.close()
ch42()