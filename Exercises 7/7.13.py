from leapyear import leap_year
from zelle712 import datechecker


def dayNumber(month, day, year):
    dayNum = 31*(month-1) + day

    if month > 2:
        dayNum = dayNum - (4 * month + 23) // 10

    if leap_year(year) and month == 2:
        dayNum = dayNum + 1

    return dayNum

def main():
    print("Day number calculation\n")

    month, day, year = input("Enter date (mm/dd/yyyy): ").split("/")
    day, month, year = int(day), int(month), int(year)

    if datechecker(month, day, year):
        print("The day number is", dayNumber(month, day, year))
    else:
        print("That's an invalid date!")

if __name__ == '__main__':
    main()


