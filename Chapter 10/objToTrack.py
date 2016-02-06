__author__ = 'Jorian'

from Projectile import Projectile
from graphics import *


def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity in Meters per second: "))
    h = eval(input("Enter the initial height in meters: "))
    t = eval(input("Enter the time interval: "))
    return a, v, h, t



def main():
    angle, vel, h0, time  = getInputs()

    win = GraphWin("Face", 600, 400)
    win.setCoords(0,0,30,30)


    objToTrack = Projectile(angle, vel, h0)
    p1 = Point(objToTrack.getX(),objToTrack.getY())

    circleTracker = Circle(p1, 0.3)
    circleTracker.setFill('red')
    circleTracker.draw(win)

    win.getMouse()

    px = objToTrack.getX()
    py = objToTrack.getY()
    while objToTrack.getY() >= 0:
        objToTrack.update(time)
        dx = objToTrack.getX() - px
        dy = objToTrack.getY() - py
        Circle(p1, 0.1).draw(win)
        p1.move(dx, dy)
        px = objToTrack.getX()
        py = objToTrack.getY()

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()