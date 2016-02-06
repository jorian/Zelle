__author__ = 'Jorian'

from Student import *


def main():
    name = input("What is the name?")
    user1 = Student(name, 0, 0)

    infoStr = input("Enter course info (gradepoints <space> credits): ")
    while infoStr != "":
        gp, credits = infoStr.split()
        user1.addLetterGrade(gp, float(credits))
        infoStr = input("Enter course info (gradepoints <space> credits): ")

    print(user1.gpa())

if __name__ == '__main__':
    main()