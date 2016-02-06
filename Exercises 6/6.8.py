__author__ = 'Jorian'
import math

def nextGuess(guess, x):
    return (guess + x/guess) / 2.0

def sqrRoot(x, iters):
    guess = x / 2.0
    for i in range(iters):
        guess = nextGuess(guess, x)
    return guess

def main():
    x = eval(input("Enter number to find the root of: "))
    n = eval(input("How many iterations should I use? "))
    print("Square root is", sqrRoot(x, n))

main()