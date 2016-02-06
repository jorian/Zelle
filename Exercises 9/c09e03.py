__author__ = 'Jorian'


def printOutcome(scoreA, scoreB):
    print("The score of team A is: ", scoreA)
    print("The score of team B is: ", scoreB)


def playOneMatch():
    scoreA = scoreB = 0
    while not gameOver(scoreA, scoreB):
        scoreA, scoreB = playOneGame


def playOneGame():
    a = b = 0
    if


def gameOver(a, b):
    if a == 15 and (a - b) > 1:
        return True
    elif b == 15 and (b - a) > 1:
        return True
    else:
        return False
