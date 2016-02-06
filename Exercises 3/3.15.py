__author__ = 'Jorian'
# Approach pi
import math
def main():
    num = int(input("How many terms would you like to sum up?"))
    total = num * 4
    mypi = 0
    for i in range(3,total,4):
        mypi = mypi + 4/(i-2) - (4/i)
    print(mypi)
    print(math.pi)
    print("Your pi with", mypi, "was ",round(mypi/math.pi*100, 2),"% accurate to",math.pi)
main()