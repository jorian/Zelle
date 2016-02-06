__author__ = 'Jorian'

from PlayingCard import *
from random import randrange

class Hand:
    def __init__(self):
        self.deck = []
        for i in range(13):
            self.deck.append(PlayingCard(i+1, 'd'))
            self.deck.append(PlayingCard(i+1, 'c'))
            self.deck.append(PlayingCard(i+1, 'h'))
            self.deck.append(PlayingCard(i+1, 's'))

    def shuffle(self):
        for i in range(len(self.deck)):
            j = randrange(i, len(self.deck))
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]


    def dealCard(self):
        return self.deck.pop(0)
        #return self.deck[0]

    def cardsLeft(self):
        return len(self.deck)


def getInputs():
    x = -1
    while True:
        x = int(input("How many numbers? "))
        if 0 < x < 53:
            return x
        else:
            print("Please enter a number 1-52")


def main():
    testhand = Hand()
    testhand.shuffle()
    x = getInputs()
    print("These cards are drawn: ")
    for i in range(x):
        print(testhand.dealCard())
    print("\nThese cards are still in the deck: ")
    for i in range(len(testhand.deck)):
        print(testhand.deck[i])
    print("Number of remaining cards:", testhand.cardsLeft())

if __name__ == '__main__':
    main()