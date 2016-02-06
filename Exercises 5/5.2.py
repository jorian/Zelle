__author__ = 'Jorian'

def quizScore():
    score = int(input("Please enter the score: "))
    scorescale = "FFDCBA"[score]
        #["F", "F", "D", "C", "B", "A"]

    if score <= 5:
        print("The score is:", scorescale)
    else:
        print("That score is out of range")
quizScore()