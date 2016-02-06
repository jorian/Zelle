__author__ = 'Jorian'

from random import random

class Student:
    """
    Simple student class which stores name, hours and qpoints.
    A GPA-score is calculated and can be retrieved.
    """
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQpoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credithrs):
        self.hours += credithrs
        self.qpoints += (gradePoint*credithrs)

    def addLetterGrade(self, letterGrade, credits):
        letter = letterGrade[0].upper()
        plusminus = letterGrade[1:].strip()
        if letter == 'A':
            score = 4.0
        elif letter == 'B':
            score = 3.0
        elif letter == 'C':
            score = 2.0
        elif letter == 'D':
            score = 1.0
        else:
            score = 0.0
        if plusminus == '+':
            score += .33
        elif plusminus == '-':
            score -= .33
        self.qpoints += score * credits
        self.hours += credits


def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    infile = open("C:/Users/Jorian/Desktop/Students.dat", 'r')
    best = makeStudent(infile.readline())
    for line in infile:
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    print("The best student is:", best.getName())
    print("Hours:", best.getHours())
    print("Qpoints:", best.getQpoints())
    print("GPA:", best.gpa())
    print(random.__doc__)
    help(random)
if __name__ == '__main__':
    main()