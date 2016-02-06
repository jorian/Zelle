__author__ = 'Jorian'


def eligibility(age, citizen):
    if age >= 25 and citizen >= 7:
        House = 'Yes'
        if age >= 30 and citizen >= 9:
            Senate = 'Yes'
        else:
            Senate = 'No'
    else:
        Senate = 'No'
        House = 'No'
    return Senate, House


def main():
    age = int(input("Please give your age: \n"))
    citizen = int(input("Please state for how many years you are citizen: \n"))

    eSenate, eHouse = eligibility(age, citizen)
    print("\nEligible for Senate: ",eSenate,"\nEligible for House: ", eHouse)

if __name__ == '__main__':
    main()