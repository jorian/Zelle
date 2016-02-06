__author__ = 'Jorian'

def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

def main():
    year = int(input("Which year do you want to know if it's a leap year?"))
    if leap_year(year):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")

if __name__ == '__main__':
    main()
