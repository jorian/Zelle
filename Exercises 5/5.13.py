__author__ = 'Jorian'

def averageLength():

    infilename = "C:/Users/Jorian/Desktop/henk.py"
    outfilename = "C:/Users/Jorian/Desktop/henkie.py"

    infile = open(infilename, "r")
    outfile = open(outfilename, "w")



    phrase = input("Enter your phrase: ")

    sumTotal = 0
    accTotal = 0
    for i in phrase.split():
        sumTotal = sumTotal + float(len(i))
        accTotal = accTotal + 1

    print("The average length of the", accTotal, "words you gave in is:", (sumTotal / accTotal))

averageLength()