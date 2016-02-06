__author__ = 'Jorian'
def main():
    squares = []
    for x in range(1,8):
        m = x*(x-1)
        squares.append(chr(m))
        print(squares)
main()