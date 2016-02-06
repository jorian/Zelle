__author__ = 'Jorian'


def fileread():
    fileName = "C:/Users/Jorian/Desktop/henk.py"
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("\nI calculated a total of", count, "numbers.")
    print("\nThe average is:", sum / count)
fileread()