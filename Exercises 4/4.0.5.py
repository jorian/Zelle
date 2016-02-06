__author__ = 'Jorian'
from graphics import *

def main():
    win = GraphWin("Tic-Tac-Toe", 600, 300)
    win.setCoords(0.0,0.0,3.0,3.0)
    Line(Point(1,0), Point(1,3)).draw(win)
    Line(Point(2,0), Point(2,3)).draw(win)
    Line(Point(0,1), Point(3,1)).draw(win)
    Line(Point(0,2), Point(3,2.5)).draw(win)
    win.getMouse()
    win.close()

main()

