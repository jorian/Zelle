__author__ = 'Jorian'

from random import randint

def main():
    n = int(input("How many flips?"))
    positionf = 0
    positions = 0
    for i in range(n):
        c = randint(1,6)
        d = randint(1,2)
        if c < 4:
            if d == 1:
                positionf = positionf - 1
            else:
                positions = positions - 1
        else:
            if d == 1:
                positionf = positionf + 1
            else:
                positions = positions + 1
    print(positionf, positions)
main()