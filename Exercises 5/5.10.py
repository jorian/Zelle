__author__ = 'Jorian'
def averageLength():
    phrase = input("Enter your phrase: ")

    sumTotal = 0
    accTotal = 0
    for i in phrase.split():
        sumTotal = sumTotal + float(len(i))
        accTotal = accTotal + 1

    print("The average length of the", accTotal, "words you gave in is:", (sumTotal / accTotal))

averageLength()