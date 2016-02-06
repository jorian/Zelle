__author__ = 'Jorian'

from graphics import *

def main():

    principal = float(input("Please enter the initial principal: "))
    apr = float(input("Please enter the annual interest rate as x.xx"))
    py = 0

    win = GraphWin('Investment Growth Chart', 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1,py), ' 0,0K').draw(win)
    Text(Point(-1,py+2500), ' 2,5K').draw(win)
    Text(Point(-1,py+5000), ' 5,0K').draw(win)
    Text(Point(-1,py+7500), ' 7,5K').draw(win)
    Text(Point(-1,py+10000), '10,0K').draw(win)

    height = principal * 0.02
    bar = Rectangle(Point(0,0), Point(1, principal))
    bar.setFill("Green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principal = principal * (1 + apr)
        xll = year * 20 + 45
        height = principal * 0.02
        bar = Rectangle(Point(year,0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

main()
