__author__ = 'Jorian'
# Fibonacci time
def main():
    n = int(input("Of which number do you want to calculate the Fibonacci number?"))
    f1 = 1
    f2 = 0
    for i in range(n):
        f3 = f2 + f1
        f1 = f2
        f2 = f3
    print("The fibonacci number of", n, "is:", f2)
main()