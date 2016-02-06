__author__ = 'Jorian'
from random import random


#def printIntro():




def main():
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def getInputs():
    a = float(input("Probability for player A: "))
    b = float(input("Probability for player B: "))
    n = eval(input("How many games to process?: "))

    return a, b, n


def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB, i):
    scoreA = 0
    scoreB = 0

    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    #print("Number of games played:", n)
    print("Player A won", winsA, "games;")
    print("Player B won", winsB, "games.")


if __name__ == '__main__':
    main()