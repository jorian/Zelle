__author__ = 'Jorian'

from graphics import *

def ch43():
    win = GraphWin("Happy Face", 240, 360)
    win.setCoords(-10,-10,10,10)

    oval = Oval(Point(-9,-8),Point(9,8))
    oval.setFill("peachpuff")
    oval.setOutline("peachpuff")

    eye1 = Oval(Point(-6,2),Point(-2,-2))
    eye1.setFill("black")

    eye2 = eye1.clone()
    eye2.move(8,0)

    nose = Oval(Point(5,5),Point(5,4))
    nose.setFill("red")

    mouth = Polygon(Point(3,4),Point(4,3),Point(6,3),Point(7,4))
    mouth.setOutline("yellow")

    oval.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    nose.draw(win)
    mouth.draw(win)

    win.getMouse()
ch43()