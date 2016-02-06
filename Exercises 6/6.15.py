__author__ = 'Jorian'
from graphics import *


# in 1 functie alles tekenen.

def drawFace(center, size, win):
    eyeSize = 0.15 * size
    eyeOff = size / 3.0
    mouthSize = 0.8 * size
    mouthOff = size / 2.0
    head = Circle(center, size)
    head.setFill("Yellow")
    head.draw(win)
    leftEye = Circle(center, eyeSize)
    leftEye.setFill("White")
    leftEye.move(-eyeOff, -eyeOff)
    rightEye = Circle(center, eyeSize)
    rightEye.setFill("White")
    rightEye.move(eyeOff, -eyeOff)
    leftEye.draw(win)
    rightEye.draw(win)
    p1 = center.clone()
    p1.move(-mouthSize / 2, mouthOff)
    p2 = center.clone()
    p2.move(mouthSize / 2, mouthOff)
    mouth = Line(p1, p2)
    mouth.draw(win)


def face():
    win = GraphWin('Draw Face', 640, 480)
    for i in range(10):
        location = win.getMouse()
        drawFace(location, 50, win)

    win.getMouse()
    win.close()


face()
