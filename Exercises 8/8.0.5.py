__author__ = 'Jorian'

# loop and a half


def posttestloop():

    while True:
        number = eval(input("enter a number: [vanilla] "))
        if number >= 0: break
        print("The number entered was not valid.")


def evaltruefalse():
    x = bool("Y")
    print(x)

def vanilla():
    flavor = input("What flavor do you want") or "vanilla"
    print(flavor)

vanilla()