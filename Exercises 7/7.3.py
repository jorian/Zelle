__author__ = 'Jorian'
def quizScore():

    score = int(input("Please enter the mark given: "))
    if 90 <= score <= 100:
        print("The score is: A")
    elif 80 <= score < 90:
        print("The score is: B")
    elif 70 <= score < 80:
        print("The score is: C")
    elif 60 <= score < 70:
        print("The score is: D")
    elif score < 60:
        print("The score is: F")
    else:
        print("That grade is incorrect!")

if __name__ == '__main__':
    quizScore()
