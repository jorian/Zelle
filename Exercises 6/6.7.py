__author__ = 'Jorian'

def calcFib(n):
    f1 = 1
    f2 = 0
    for i in range(n):
        f3 = f2 + f1
        f1 = f2
        f2 = f3
    return f3

def main():
    n = int(input("Of which number do you want to calculate the Fibonacci number?"))

    print("The fibonacci number of", n, "is:", calcFib(n))
main()