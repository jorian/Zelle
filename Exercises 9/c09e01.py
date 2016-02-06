__author__ = 'Jorian'
# c09ex01.py
#  Racquetball best of n games

from random import random

def main():
    printIntro()
    probA, probB, n, matches = getInputs()
    winsA, winsB, shotA, shotB = simMatches(matches, n, probA, probB)
    printSummary(winsA, winsB, shotA, shotB)

def printIntro():
    # Prints an introduction to the program
    print("This program simulates racquetball matches between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("serves first in the first game of a match, and the first")
    print("service alternates in subsequent games. \n")

def getInputs():
    # RETURNS probA, probB, number of games to simulate
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games are in a match? "))
    m = eval(input("How many matches should be simulated? "))
    return a, b, n, m

def simMatches(howMany, n, probA, probB):
    # Simulates n games of racquetball between players A and B
    # RETURNS number of wins for A, number of wins for B
    winsA = winsB = 0
    for i in range(howMany):
        gamesA, gamesB, shotA, shotB = simOneMatch(n, probA, probB)
        if gamesA > gamesB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB, shotA, shotB

def simOneMatch(n, probA, probB):
    gamesA = gamesB = 0
    sA = sB = 0
    needed = n/2 + 1
    while gamesA < needed and gamesB < needed:
        # Alternate serves, A serves first game of match
        if (gamesA + gamesB) % 2 == 1:
            firstServe = "A"
        else:
            firstServe = "B"
        scoreA, scoreB = simOneGame(probA, probB, firstServe)
        shotA, shotB = shoutout(scoreA, scoreB)
        if scoreA > scoreB:
            gamesA = gamesA + 1
            if shotA == True:
                sA = sA + 1
        else:
            gamesB = gamesB + 1
            if shotB == True:
                sB = sB + 1
    return gamesA, gamesB, sA, sB

def simOneGame(probA, probB, Server):
    # Simulates a single game or racquetball between players A and B
    # RETURNS A's final score, B's final score
    serving = Server
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

def shoutout(scoreA, scoreB):
    shotA = shotB = False
    if scoreA == 15 and scoreB == 0:
        shotA = True
    elif scoreB == 15 and scoreA == 0:
        shotB = True
    return shotA, shotB

def gameOver(a,b):
    # a and b are scores for players in a racquetball game
    # RETURNS true if game is over, false otherwise
    return a == 15 or b == 15


def printSummary(winsA, winsB, shotA, shotB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nMatches simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    if winsA == 0:
        print("Shotouts for A: 0")
    else:
        print("Shotouts for A: {0} ({1:0.1%})".format(shotA, shotA/winsA))
    if winsB == 0:
        print("Shotouts for B: 0")
    else:
        print("Shotouts for B: {0} ({1:0.1%})".format(shotB, shotB/winsB))
if __name__ == "__main__": main()





