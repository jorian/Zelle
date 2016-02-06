__author__ = 'Jorian'

def sumN(n):
    nadd = 0
    for i in range(1, n+1):
        nadd = nadd + i
        #print(nadd,end=" ")
    return nadd

def sumNCubes(n):
    nadd = 0
    for i in range(1, n+1):
        nadd = nadd + i**3
    return nadd

def main():
    print("This program computes the sum and sum of cubes of the first")
    print("N natural numbers.\n")

    n = eval(input("Please enter a value for N: "))
    print("The sum of the first %d natural numbers is %d" % (n,sumN(n)))
    print("The sum of the cubes of those numbers is %d" % (sumNCubes(n)))

main()

