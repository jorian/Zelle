__author__ = 'Jorian'
def main():
    print("This program calculates interest")
    principal = eval(input("Startbedrag: "))
    jrp = eval(input("Jaarlijks rentepercentage: "))
    for i in range(10):
        principal = principal * (1 + (jrp / 100))
    print("Het eindbedrag is", principal)
main()