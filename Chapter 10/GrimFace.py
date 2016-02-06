__author__ = 'Jorian'

from graphics import *
from DieAndButton import Button

class Face:
    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, -mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, -mouthOff)
        p3 = center.clone()
        p3.move(-eyeOff, eyeOff)
        p4 = p3.clone()
        p4.move(eyeOff,0)
        self.mouth = Line(p1, p2)
        self.mouth.draw(window)
        self.window = window
        self.leftEye1 = Line(p3, p4)



    def wink(self):
        self.leftEye.undraw()
        self.leftEye = self.leftEye1
        self.leftEye.draw(self.window)





def main():
    win = GraphWin("Face", 600, 400)
    win.setCoords(0,0,15,15)
    pt = win.getMouse()
    face = Face(win, pt, 3)
    bWink = Button(face.window, Point(13, 13), 3, 1, "Wink")
    bWink.activate()
    quitButton = Button(face.window, Point(13, 2), 3, 1, "Quit")
    quitButton.activate()


    while not quitButton.clicked(pt):
        if bWink.clicked(pt):
            face.wink()
        pt = win.getMouse()


if __name__ == '__main__':
    main()