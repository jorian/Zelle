__author__ = 'Jorian'

def acronym():
    phrase = str(input("Enter the words you want an acronym of: "))

    acro = ""
    for i in phrase.split():
        acro = acro + i[0]
    acro = acro.upper()
    print(acro)


acronym()