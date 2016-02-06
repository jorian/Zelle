__author__ = 'Jorian'

def main():
    n = int(input("Give the number from which you want the sum of:"))
    nadd = 0
    for i in range(n):
        nadd = nadd + i**3
        print(nadd)
main()