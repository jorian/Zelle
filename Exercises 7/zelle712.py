__author__ = 'Jorian'


def datechecker(month, day, year):
    if 0 < month <= 12:
        if month in [4,6,9,11] and day == 31:
            return False
        else:
            return True
    else:
        return False


def main():
    month, day, year = input("Please enter a date, divided with / ").split("/")
    print(datechecker(int(month), int(day), int(year)))

if __name__ == '__main__':
    main()