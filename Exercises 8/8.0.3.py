__author__ = 'Jorian'


def booleans():
    a = 0
    b = 0
    z = (a >= 15 or b >= 15) and (abs(b - a >= 2))
    y = a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and a == 0)
    while a != 15 and b != 15:
        a = a + 1
        b = b + 1
        print(a,b)



booleans()
