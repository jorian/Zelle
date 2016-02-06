__author__ = 'Jorian'
from graphics import *

def barchart():


    infile = open("C:/Users/Jorian/Desktop/henk.py", "r")

    y = int(infile.readline())*2+1

    win = GraphWin('Investment Growth Chart', 640, 480)
    win.setBackground("white")
    win.setCoords(0, 0, 85, y)

    temp = 0


    #list = infile.readlines()
    #noStudents = int(list[0])
    #print(noStudents)

    for line in infile:
        name, scores = line.split()
        namePos = (y - 1.5) - 1 * temp

        title = Text(Point(8,namePos),"{:<10}".format(name))
        title.draw(win)

        scores = int(scores)+15

        barUL = (y-1)-1*temp
        barLR = (y-2)-1*temp

        graph = Rectangle(Point(15,barUL),Point(scores*0.7,barLR))
        graph.setFill('green')
        graph.draw(win)

        temp = temp+2

    infile.close()
    win.getMouse()
    win.close()


barchart()