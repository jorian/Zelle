__author__ = 'Jorian'


def quizScore():

    score = int(input("Please enter the mark given: "))
    if score == 5:
        print("The score is: A")
    elif score == 4:
        print("The score is: B")
    elif score == 3:
        print("The score is: C")
    elif score == 2:
        print("The score is: D")
    elif score <= 1:
        print("The score is: F")
    else:
        print("That grade is incorrect!")


# Dictionary! :
def f(x):
    return {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
    }[x]


def main():
    score = int(input("Please enter the mark: "))
    print(f(score))

if __name__ == '__main__':
    main()
