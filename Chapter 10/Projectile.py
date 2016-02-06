__author__ = 'Jorian'

from math import radians, cos, sin

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ymax = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def getYmax(self):
        return self.ymax

    def update(self, time):
        self.xpos += time * self.xvel
        yvel1 = self.yvel - time *9.81
        self.ypos += time * (self.yvel + yvel1)/2.0     #for average velocity
        self.yvel = yvel1
        if self.ymax < self.ypos:
            self.ymax = self.ypos

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity in Meters per second: "))
    h = eval(input("Enter the initial height in meters: "))
    t = eval(input("Enter the time interval: "))
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print('\nDistance traveled: {0:0.1f} meters. Highest point: {1:0.1f} meters.'.format(cball.getX(),cball.getYmax()))


if __name__ == '__main__':
    main()