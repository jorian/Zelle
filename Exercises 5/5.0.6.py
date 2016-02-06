__author__ = 'Jorian'

def main():
    print("This program ocnverts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    inString = input("Please enter the unicode encoded message: ")

    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)
        message = message + chr(codeNum)
    print('\nThe decoded message is', message)
main()