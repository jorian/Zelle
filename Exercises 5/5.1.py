__author__ = 'Jorian'


def dateconvert():
    day, month, year = eval(input("Enter day, month, year in numbers"))
    date1 = "{1}/{0}/{2}".format(month, day, year)
    months = ["January", "February", "March", "April", "May", "June",
              "July", "Augustus", "September", "October", "November", "December"]

    date2 = "{0} {1}, {2}".format(months[month - 1], day, year)

    print("The date is {0} or {1}.".format(date1, date2))


dateconvert()
