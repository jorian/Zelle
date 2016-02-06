__author__ = 'Jorian'

def function():

    hours = float(input("Please enter the total amount of hours worked this week: "))
    wage = float(input("Please enter the hourly wage: "))
    if hours > 40.0:
        n = hours - 40.0
        print("You earned a total of: €{0:0.2f}".format((n * (wage*1.5)) + (wage * 40.0)))
    else:
        print("You earned a total of: €{0:0.2f}".format(wage * hours))

if __name__ == '__main__':
    function()