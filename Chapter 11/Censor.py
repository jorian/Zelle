__author__ = 'Jorian'

def autocensor():
    fileName = "C:/Users/Jorian/Desktop/Text.dat"
    infile = open(fileName, 'r')
    writefile = open("C:/Users/Jorian/Desktop/TextWrite.dat", 'w')
    line = infile.readline()
    templist = []
    while line != "":
        for xStr in line.split():
            templist.append(xStr)
        for i in range(len(templist)):
            if len(templist[i]) == 4:
                templist[i] = "****"
        templist.append("\n")
        line = infile.readline()
    print(" ".join(templist), file=writefile)

autocensor()