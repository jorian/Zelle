__author__ = 'Jorian'


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
        # return strList


def sumList(numbers):
    nums = 0
    for i in range(len(numbers)):
        nums = nums + numbers[i - 1]
    return nums


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums


def main():
    infile = open("C:/Users/Jorian/Desktop/henk.py", "r").readlines()

    toNumbers(infile)
    squareEach(infile)
    print("The sum is: ",sumList(infile))


main()