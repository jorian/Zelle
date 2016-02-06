__author__ = 'Jorian'

def wc():

    infile = open("C:/Users/Jorian/Desktop/henk.py", "r")
    #outfile = open("C:/Users/Jorian/Desktop/henk.py", "w")
    chars = infile.read()
    infile.close()

    words = chars.split()
    lines = chars.split("\n")
    #outfile.close()

    print("This document has:\n", len(lines), "lines,\n", len(words), "words and\n", len(chars), "characters.")

wc()