__author__ = 'Jorian'

from random import randrange


def main():
    printIntro()
    n = getInputs()
    winsDealer, winsPlayer, blackJacks = simNBlackjack(n)
    printSummary(n, winsDealer, winsPlayer, blackJacks)


def printIntro():
    print("This is a game of BlackJack. This program calculates the probability")
    print("of the winning chances of the Dealer.")


def getInputs():
    n = int(input("How many games to play? "))
    return n


def simNBlackjack(n):
    winsDealer = 0
    winsPlayer = 0
    blackJacks = 0

    for i in range(n):
        scoreDealer, scorePlayer, turns = simOneBJGame()
        if scoreDealer > scorePlayer:
            if scoreDealer <= 21:
                winsDealer = winsDealer + 1
                print("Dealer won")

            else:
                winsPlayer = winsPlayer + 1
                print("Player won")
        else:
            if scorePlayer < 21:
                winsPlayer = winsPlayer + 1
                print("Player won")
            elif scorePlayer == 21 and turns == 4:
                print("Player has BlackJack!!!")
                blackJacks = blackJacks + 1
            else:
                winsDealer = winsDealer + 1
                print("Dealer won")

    return winsDealer, winsPlayer, blackJacks


def simOneBJGame():
    scoreDealer = scorePlayer = 0
    turn = "Dealer"
    turns = 0
    while not gameOver(scoreDealer, scorePlayer, turn, turns):
        if turn == "Player":
            card, hasAce = getCard()
            if hasAce == True:
                if scorePlayer >= 11:
                    scorePlayer = scorePlayer + 1
                elif scorePlayer < 11:
                    scorePlayer = scorePlayer + 11
            else:
                scorePlayer = scorePlayer + card
            print("Turn:", turn)
            print("ScoreDealer:", scoreDealer)
            print("ScorePlayer:", scorePlayer, "\n")
            turn = "Dealer"
            turns = turns + 1
        elif turn == "Dealer":
            card, hasAce = getCard()
            if hasAce and scoreDealer + card >= 17:
                scoreDealer = scoreDealer + 11
            elif hasAce and scoreDealer + card < 17:
                scoreDealer = scoreDealer + 1
            else:
                scoreDealer = scoreDealer + card
            print("Turn:", turn)
            print("ScoreDealer:", scoreDealer)
            print("ScorePlayer:", scorePlayer, "\n")
            turn = "Player"
            turns = turns + 1
    return scoreDealer, scorePlayer, turns


def gameOver(scoreDealer, scorePlayer, turn, turns):
    if 16 < scoreDealer < 22 and scorePlayer < scoreDealer and turn == "Dealer":
        return False
    elif 16 < scoreDealer < 22 and scorePlayer > scoreDealer:
        return True
    elif scoreDealer > 21:
        return True
    elif scorePlayer == 21 and turns == 4:
        return True
    elif scorePlayer > 21:
        return True
    else:
        return False


def getCard():
    card = 0
    cardValue = randrange(1, 14)
    hasAce = False
    if cardValue > 10:
        card = 10
    elif cardValue == 1:
        hasAce = True
    else:
        card = cardValue
    return card, hasAce


def printSummary(n, winsDealer, winsPlayer, blackJacks):
    print(n, "games were played.\n")
    print("The dealer won", winsDealer, "times.")
    print("The player won", winsPlayer, "times.")
    print("A total of", blackJacks, "blackjacks were seen in this game.")
    print("The probability of the dealer winning is:", (winsDealer / n) * 100,"%")


if __name__ == '__main__':
    main()