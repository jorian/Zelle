__author__ = 'Jorian'

from random import randrange

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

def main():
    die1 = MSDie(6)
    die1.help()
    print(die1.value)

if __name__ == '__main__':
    main()