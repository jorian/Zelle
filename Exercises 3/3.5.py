__author__ = 'Jorian'
# Calculate the cost of ordering coffee.
# 1 pound costs 10.50, shipping costs 0.86 per pound. Each order has 1.50 overheadcosts.

def main():
    pounds = float(input("How many pounds of coffee would you like? "))
    coffee = 10.50
    shipping = 0.86
    overhead = 1.50
    totalprice = (pounds * coffee) + (pounds * shipping) + overhead
    print("The total price is: E", totalprice)
main()