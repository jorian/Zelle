__author__ = 'Jorian'


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
        # return strList


def stringList():
    x = ["14", "12"]
    toNumbers(x)
    print(x)


stringList()
