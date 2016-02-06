__author__ = 'Jorian'


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums


def numbers():
    nums = [14, 25, 32, 63, 546, 32, 54, 34, 6, 72, 541, 321, 352, 323, 12, 352, 12, 21, ]
    print(squareEach(nums))


numbers()
