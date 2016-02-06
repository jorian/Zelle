__author__ = 'Jorian'

from math import *


def getNumbers():
    nums = []

    xStr = input("Enter a number")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)
        xStr = input("Enter a number")
    return nums


def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)


def meanStdDev(nums):
    xbar = mean(nums)
    sumDevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumDevSq += dev * dev
    stdDev = sqrt(sumDevSq / (len(nums) - 1))
    return xbar, stdDev


def stdDev(nums):
    xbar, stdDev = meanStdDev(nums)
    return stdDev


def main():
    data = getNumbers()
    xbar, stdDev = meanStdDev(data)
    print("The mean is", mean(data))
    print("{0} {1}".format(xbar, stdDev))


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos - 1]) / 2
    else:
        median = nums[midPos]
    return median


if __name__ == '__main__': main()
