__author__ = 'Jorian'

from random import random


def main():
    d1, d2, d3, d4, d5, rolls = rolvijfDobbelstenen()
    printOutput(d1, d2, d3, d4, d5, rolls)


def rolvijfDobbelstenen():
    d1 = d2 = d3 = 5
    d4 = d5 = 0
    rolls = 0
    while not fiveTheSame(d1, d2, d3, d4, d5):
        d1 = 1 + int(random() / (1/6))
        d2 = 1 + int(random() / (1/6))
        d3 = 1 + int(random() / (1/6))
        d4 = 1 + int(random() / (1/6))
        d5 = 1 + int(random() / (1/6))
        rolls = rolls + 1
    return d1, d2, d3, d4, d5, rolls


def fiveTheSame(d1, d2, d3, d4, d5):
    if d1 == d2 == d3 == d4 == d5:
        return True
    else:
        return False


def printOutput(d1, d2, d3, d4, d5, rolls):
    print(d1, d2, d3 ,d4 ,d5)
    print("Probability: ", (1/rolls) * 100,"%")

if __name__ == '__main__':
    main()