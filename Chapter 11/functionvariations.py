__author__ = 'Jorian'
from random import randrange

def count(myList, x):
    occ = 0.0
    for i in myList:
        if i == x:
            occ += 1
    return occ


def isin(myList, x):
    occ = False
    for i in myList:
        if i == x:
            occ = True
    return occ


def index(myList, x):
    acc = 0
    for i in myList:
        acc += 1
        if i == x:
            return acc


def reverse(lst):
    for i in range(int(len(lst)/2)):
        j = -(i+1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

    # l = len(mylist)
    # o = 0
    # newList = []
    # for i in mylist:
    #     print(l)
    #     newList[o] = mylist[i]
    #     l -= 1
    #     o += 1


def sort(myList):
    a = 97
    newList = []
    for b in range(0, 27):
        for i in myList:
            if i[0].lower() == chr(a):
                newList.append(i)
        a += 1
    return newList


def shuffle(myList):
    for i in range(len(myList)):
        j = randrange(i,len(myList))
        print(j)
        myList[i], myList[j] = myList[j], myList[i]
    return myList


def innerProduct():
    x = [1, 5, 6, 48, 56, 789, 56, 7, 56, 32]
    y = [45, 89, 45, 75, 78, 23, 10, 15, 19, 88]
    z = 0
    for i in range(len(x)):
        z += x[i-1] * y[i-1]
    print(z)


def removeDuplicates():
    x = [45, 89, 45, 75, 78, 23, 10, 15, 19, 88, 23, 45, 12, 35, 23, 12, 556, 12, 512]
    y = []
    for i in range(len(x)):
        if not x[i] in y:
            y.append(x[i])
    print(y)




def main():
    list1 = list(range(30))
    # ["henk", "piet", "klaas", "adolf", "jorian", "johannes"]
    #searchname = input("What to search for?")
    #counter = count(list, searchname)
    #present = isin(list, searchname)
    #num = index(list, searchname)
    shuffledList = shuffle(list1)

    print(shuffledList)

if __name__ == '__main__':
    removeDuplicates()