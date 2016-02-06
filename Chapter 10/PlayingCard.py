__author__ = 'Jorian'

from random import randrange

class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        if self.rank < 10:
            return self.rank
        else:
            return 10

    def __str__(self):
        ranks = [None, "Ace", "Two", "Three", "Four", "Five", "Six",
                 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        rankStr = ranks[self.rank]
        if self.suit == 'd':
            card = 'Diamonds'
        elif self.suit == 'h':
            card = 'Hearts'
        elif self.suit == 'c':
            card = 'Clubs'
        else:
            card = 'Spades'
        return "{0} of {1}".format(rankStr, card)


def main():
    n = int(input("How many cards to evaluate?"))
    for i in range(n):
        suit = "dchs"[randrange(4)]
        rank = randrange(1,14)
        s = PlayingCard(rank, suit)
        print(s)
        print("The BlackJack value is:", s.BJValue())

if __name__ == '__main__':
    main()

