__author__ = 'Jorian'
# Calculate epact
def main():
    year = int(input("To figure out the day of Easter, please give the year: "))
    C = year // 100
    epact = (8 + (C//4) - C + ((8 * C + 13)//25) + 11 * (year % 19)) % 30
    print("the epact is:", epact)
main()