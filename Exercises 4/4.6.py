__author__ = 'Jorian'
from graphics import *

def main():

    win = GraphWin('Investment Growth Chart', 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)

    t1 = Text(Point(4,9000), "Enter Principal:")
    t1.draw(win)

    t2 = Text(Point(4,7000), "Enter APR:")
    t2.draw(win)

    principal = (Entry(Point(6,9000),5))
    principal.setText("0")
    principal.draw(win)

    apr = Entry(Point(6,7000), 5)
    apr.setText("0.00")
    apr.draw(win)

    win.getMouse()

    principal2 = float(principal.getText())
    apr2 = float(apr.getText())

    principal.undraw()
    apr.undraw()
    t1.undraw()
    t2.undraw()

    py = 0
    pz = 2500

    Text(Point(-1,py), ' 0,0K').draw(win)
    Text(Point(-1,py+pz), ' 2,5K').draw(win)
    Text(Point(-1,py+pz+pz), ' 5,0K').draw(win)
    Text(Point(-1,py+pz+2500), ' 7,5K').draw(win)
    Text(Point(-1,py+pz+5000), '10,0K').draw(win)

    height = principal2 * 0.02
    bar = Rectangle(Point(0,0), Point(1, principal2))
    bar.setFill("Green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principal2 = principal2 * (1 + apr2)
        bar = Rectangle(Point(year,0), Point(year+1, principal2))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

main()