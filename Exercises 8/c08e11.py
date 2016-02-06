__author__ = 'Jorian'

def main():
    print("Heating and Cooling degree-day calculation.\n")

    infile = open("C:/Users/Jorian/Desktop/henk.py", "r")

    heating = 0.0
    cooling = 0.0
    #tempStr = infile.readlines()
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            temp = eval(xStr)
            heating = heating + max(0, 60-temp)
            cooling = cooling + max(0, temp-80)
        line = infile.readline()
        #tempStr = input("Enter an average daily temperature: ")

    print("\nTotal heating degree-days", heating)
    print("Total cooling degree-days", cooling)

if __name__ == '__main__':
    main()
