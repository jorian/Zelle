__author__ = 'Jorian'

from PlayingCard import *

def createlist():
    filename = "C:/Users/Jorian/Desktop/Cards.dat"
    infile = open(filename, 'r')
    listCards = []
    for line in infile:
        rank, suit = line.split()
        card = PlayingCard(int(rank), suit)
        listCards.append(card)

    listCards.sort(key=PlayingCard.getRank)
    #listCards.sort(key=PlayingCard.getSuit)

    for card in listCards:
        print(card)

if __name__ == '__main__':
    createlist()

