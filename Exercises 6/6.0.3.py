__author__ = 'Jorian'

from graphics import *

def drawBar(window, year, height):
    #Draw a bar in window starting at year with given height
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    principal = float(input("Please enter the initial principal: "))
    apr = float(input("Please enter the annual interest rate as x.xx: "))

    win = GraphWin('Investment Growth Chart', 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1,0), ' 0,0K').draw(win)
    Text(Point(-1,2500), ' 2,5K').draw(win)
    Text(Point(-1,5000), ' 5,0K').draw(win)
    Text(Point(-1,7500), ' 7,5K').draw(win)
    Text(Point(-1,10000), '10,0K').draw(win)

    drawBar(win,0,principal)
    for year in range(1,11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)
    win.getMouse()
    win.close()
main()
