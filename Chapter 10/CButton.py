__author__ = 'Jorian'

from graphics import *


class CButton:
    def __init__(self, win, center, radius, label):

        self.cx = center.getX()
        self.cy = center.getY()
        self.circ = Circle(center, radius)
        self.circ.draw(win)
        self.circ.setFill('gray')
        self.rsquare = radius * radius
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        dx = p.getX() - self.cx
        dy = p.getY() - self.cy
        return self.active and dx*dx + dy*dy <= self.rsquare

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('lightgrey')
        self.circ.setWidth(1)
        self.active = False
