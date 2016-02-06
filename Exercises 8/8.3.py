__author__ = 'Jorian'


def interestdoubler():
    initinvestment = int(input("Please enter the investment: "))
    investment = initinvestment
    years = 0
    apr = float(input("Please enter the amount of interest: "))

    while investment <= (initinvestment * 2):
        investment = investment * (1 + apr)
        years = years + 1
        print(years, "||", investment)
    print("\nAfter", years, "years, the investment has doubled.")
interestdoubler()