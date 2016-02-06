__author__ = 'Jorian'

def syracuse(x):

    x = int(input("Please enter a number to start the Syracuse sequence: "))

    while x >= 2:
        if x % 2 == 0:
            x = x / 2
        else:
            x = (3 * x) + 1
        print(int(x),end=" ")

syracuse()