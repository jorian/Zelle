__author__ = 'Jorian'
def main():
    first = input("Please enter your first name in lowercase letters: ")
    last = input("Please enter your last name in lowercase letters: ")

    uname = first[0] + last[:7]

    print("Your username is", uname)
main()