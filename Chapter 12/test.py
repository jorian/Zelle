__author__ = 'Jorian'

from Poker import *

def main():
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()

if __name__ == '__main__':
    main()