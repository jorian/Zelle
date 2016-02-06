__author__ = 'Jorian'

def whileloop():
    sum = 0.0
    count = 0
    xStr = input("Enter a number: ")
    while xStr != "":
        x = eval(xStr)
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number: ")
    print("The average is:", sum / count)
whileloop()