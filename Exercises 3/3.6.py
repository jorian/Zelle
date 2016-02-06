__author__ = 'Jorian'
import math
def main():
    ptx1, pty1 = int(input("Give the first two points, separated by a comma: "))
    ptx2, pty2 = int(input("Give the second two points, separated by a comma: "))
    slopex = (ptx2 - ptx1)**2
    slopey = (pty2 - pty1)**2
    print("The slope is", slopey, '/', slopex)
    distance = math.sqrt(slopex + slopey)
    print("The distance between these points is: ", distance)
main()