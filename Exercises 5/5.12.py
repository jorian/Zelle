__author__ = 'Jorian'
def futval():
    print("This program calculates the future value of a yearly investment")
    print()

    investment = eval(input("Enter amount to invest each year: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))
    print()
    print("{0:^5} {1:^7}".format("Years", "Value"))
    for i in range(years):
        investment = investment * (1 + (0.01 * apr))
        #principal = (principal + payment) * (1 + apr)
        print("{0:^5}  €{1:4.2f}".format((i+1), investment))
    #print("The amount in", years, "years is:", principal)

futval()
