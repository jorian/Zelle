__author__ = 'Jorian'
from graphics import *

def main():

    #read file from disk
    infile = open('C:/Users/Jorian/Desktop/henk.py','r')

    #create 11 items in List as accumulator variable for scores 0-10
    scores = [0,0,0,0,0,0,0,0,0,0,0]

    #for counting total students
    students = 0

    #loop through each line and use list index as counter for
    #each scores number
    for line in infile:
        scores[int(line)] = scores[int(line)]+1
        students = students+1

    height = max(scores)

    # 1 Coord = 10px
    # each score bar height increse 10px too.
    win = GraphWin('Quiz Score Result',640,480)
    win.setCoords(0,0,35,height*1.5)


    #draw black bottom background part
    bottomBG = Rectangle(Point(0,0),Point(35,4))
    bottomBG.setFill('black')
    bottomBG.draw(win)


    #draw CLOSE button (fake button) with shadow and text
    buttonShadow = Rectangle(Point(27.5,0.5),Point(34.5,3))
    buttonShadow.setFill(color_rgb(63,63,63))
    buttonShadow.draw(win)

    buttonBox = Rectangle(Point(27.25,0.75),Point(34.25,3.25))
    buttonBox.setFill(color_rgb(155,155,155))
    buttonBox.draw(win)

    buttonText = Text(Point(30.75,2),'Close')
    buttonText.setFill('White')
    buttonText.draw(win)

    #show total students
    students = 'Total Students: '+str(students)

    print(students)
    totalStudent = Text(Point(8,2),students)
    totalStudent.setFill('white')
    totalStudent.draw(win)

    # horizon arm
    Line(Point(1,5),Point(34.5,5)).draw(win)

    # vertical arm
    Line(Point(1,5),Point(1,height*1.4)).draw(win)

    #small indicator(1-20)
    for i in range(6,height+7):
        Line(Point(1,i),Point(1.3,i)).draw(win)

    #longer indicator (5,10,15,20)
    for i in range(10,height+20,5):
        Line(Point(1,i),Point(1.9,i)).draw(win)



    #create bar chart using List index
    pos = 2
    for i in range(11):
        bar = Rectangle(Point(pos,5),Point(pos+2,scores[i]+5))
        bar.setFill('red')
        bar.draw(win)

        pos = pos+3

    #bar number 0-10
    position = 3
    for i in range(11):
        Text(Point(position,6),i).draw(win)
        position = position+3

    win.getMouse()
    win.close()

main()