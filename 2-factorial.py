__author__ = 'Jorian'
def main():
    fact = 1
    invoer = eval(input("Voer hier het getal in: "))
    for factor in range(invoer,1,-1):
        fact = fact * factor
    print("De factorial is: ",fact)
    var = sqrt(4.5-5.0)+7*3
    print(var)
main()