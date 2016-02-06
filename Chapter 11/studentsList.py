__author__ = 'Jorian'

from Student import *

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for (name, chours, cpoints) in infile:
        students.append((name, chours, cpoints))
    infile.close()
    return students


def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQpoints()), file=outfile)
    outfile.close()


def main():
    print(readStudents("C:/Users/Jorian/Desktop/Students.dat"))

    # file = "C:/Users/Jorian/Desktop/Students.dat"
    # data = readStudents(file)
    # toFilter = input("Where to filter on? gpa, qpoints, name or hours?")
    # re = input("Do you want this in reversed order?")
    # order = re[0].lower() in ['y', 'j']
    #
    # if toFilter[0].lower() == 'g':
    #     data.sort(key=Student.gpa, reverse=order)
    # elif toFilter[0].lower() == 'h':
    #     data.sort(key=Student.getHours, reverse=order)
    # elif toFilter[0].lower() == 'n':
    #     data.sort(key=Student.getName, reverse=order)
    # else:
    #     toFilter[0].lower() == 'q'
    #     data.sort(key=Student.getQpoints, reverse=order)
    #
    # file = "C:/Users/Jorian/Desktop/Students-2.dat"
    # writeStudents(data, file)


if __name__ == '__main__':
    main()