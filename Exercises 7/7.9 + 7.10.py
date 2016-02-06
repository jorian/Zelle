__author__ = 'Jorian'
# Easter


def calculate_easter(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b+4*c+6*d+5)%7

    easter_date = 0 + d + e
    return easter_date


def main():
    year = int(input("For which year do you want to calculate Easter? \n"))

    if year in [1954, 1981, 2049, 2076]:
        calculated_days = calculate_easter(year) - 7
    else:
        calculated_days = calculate_easter(year)

    if calculated_days <= 8:
        print("Easter is on March", 22 + calculated_days)
    else:
        print("Easter is on April", calculated_days - 8)

if __name__ == '__main__':
    main()