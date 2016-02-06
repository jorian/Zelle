__author__ = 'Jorian'
import graphics
from graphics import *


win = GraphWin('Shapes', 320, 240)

center = Point(100,100)
center.setFill('blue')
center.draw(win)

radius = 60

circ = Circle(center, radius)
circ.setFill('red')
circ.draw(win)

label = Text(center, "Red Circle")
label.draw(win)

rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)


center2 = center.clone()
c1 = center2.move(5,8)
c2 = center2.draw(win)

line = Line(Point(20,30), Point(180,165))
line.draw(win)

oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)


win.getMouse()
win.close()

