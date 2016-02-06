__author__ = 'Jorian'
from graphics import *

def main():

    infile = open("C:/Users/Jorian/Desktop/henk.py", "r")

    students = infile.readline()

    print(students)

    y = int(students)*2+1

    win = GraphWin('Student Exams Chart',480,y*20)
    win.setCoords(0,0,16,y)
    win.setBackground('White')

    temp = 0

    for i in infile:
        name,scores = i.split()

        namePos = (y-1.5)-1*temp

        title = Text(Point(2,namePos),'{:<10}'.format(name))
        title.draw(win)

        # since bar start x=5 so must +5 plus every point*0.1coords
        scores = int(scores)*0.1+5

        # use temp to draw space between each bar
        barUL = (y-1)-1*temp
        barLR = (y-2)-1*temp

        graph = Rectangle(Point(5,barUL),Point(scores,barLR))
        graph.setFill('green')
        graph.draw(win)

        temp = temp+2


    infile.close()
    win.getMouse()
    win.close()

main()