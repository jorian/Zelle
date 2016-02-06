__author__ = 'Jorian'


def sumList(numbers):
    nums = 0
    for i in range(len(numbers)):
        nums = nums + numbers[i - 1]
    return nums


def numbers():
    numbers = [14, 25, 32, 63, 546, 32, 54, 34, 6, 72, 541, 321, 352, 323, 12, 352, 12, 21, ]
    print("The sum of this list is:", sumList(numbers))


numbers()
