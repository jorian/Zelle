__author__ = 'Jorian'
# Calculate the cost per square inch of a circular pizza, given its diameter and price.
import math

def pricePizza(diameter, price):
    return float(price) / areaPizza(diameter)

def areaPizza(diameter):
    return math.pi * (diameter / 2) ** 2

def main():
    diameter = float(input("What is the diameter? "))
    price = float(input("What is the price?"))
    # inch = 0.393700787
    #area = (math.pi * (diameter / 2) ** 2)
    #area = areaPizza(diameter)
    #price = pricePizza(price)
    #priceperinch = price / area
    print("Price per inch is:", pricePizza(diameter, price))
main()

