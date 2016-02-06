__author__ = 'Jorian'

def creditclassification():
    credits = abs(int(input("Please enter the credits: ")))
    if credits < 7:
        print("Freshman")
    elif 7 <= credits < 16:
        print("Sophomore")
    elif 16 <= credits < 26:
        print("Junior")
    else:
        print("Senior")

if __name__ == '__main__':
    creditclassification()