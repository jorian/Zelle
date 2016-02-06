__author__ = 'Jorian'
def main():
    n = int(input("How many numbers do you want to average?"))
    total = 0
    for i in range(n, 0, -1):
        s = float(input("Enter your number:"))
        total = total + s
    print((float(total / n)))
main()