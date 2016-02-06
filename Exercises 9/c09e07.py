__author__ = 'Jorian'

from random import random

def rolTweeDobbelstenen():
    d1 = 1 + int(random() / (1/6))
    d2 = 1 + int(random() / (1/6))

    pips = d1 + d2
    return pips


def gameWon(match):
    pips = rolTweeDobbelstenen()
    initialRoll = pips
    #return pips == 7 or pips == 11
    if initialRoll == 7 or initialRoll == 11:
        return True
    elif initialRoll == 2 or 3 or 12:
        return False
    elif match == 2 and pips == 7:
        return False
    elif match > 2 and pips == initialRoll:
        return True


def game():
    match = 1
    if gameWon(match):
        #pips = rolTweeDobbelstenen()
        #print(pips)
        #match = match + 1
        print("Player Won. Initial roll was: ", initialRoll, ", the game was won with ", pips, "pips")
    elif not gameWon(pips, initialRoll, match):
        print("The player lost.")

def output(tries):
    print("Player won after", tries, " tries.")

game()



