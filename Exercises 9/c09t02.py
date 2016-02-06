__author__ = 'Jorian'

from random import random

def halfomhalf():
    for i in range(100):
        if int(random() * 10) % 2 == 0:
            print(random() * 0.5)
        else:
            print(random() * (-0.5))

def rolTweeDobbelstenen():
    for i in range(50):
        d1 = 1 + int(random() / (1/6))
        d2 = 1 + int(random() / (1/6))
        print(d1 + d2)

def main():
    for i in range(100):
        if int(random() * 10) % 2 == 0:
            print(random() * 10)
        else:
            print(random() * (-10))

tweedobbelstenen()