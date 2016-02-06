__author__ = 'Jorian'
from graphics import *

def test2():
    win = GraphWin("Henk")
    shape = Rectangle(Point(50,50), Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
    win.getMouse()
    win.close()
test2()
