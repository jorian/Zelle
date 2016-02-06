__author__ = 'Jorian'
#Greatest Common Divisor

def gcd(m, n):

    while m != 0:
        n, m = m, n%m
        print(n, m)
    return n

def main():

    m = int(input("Please enter the first number: "))
    n = int(input("Please enter the second number: "))

    print(gcd(m,n), "\nis the GCD.")
main()