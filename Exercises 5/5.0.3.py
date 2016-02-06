__author__ = 'Jorian'
def main():
    inString = input("Please enter the numbers to encode: ")
    #       inString.split()

    chars = []
    for numStr in inString.split():
        convNum = eval(numStr)
        chars.append(chr(convNum))

    message = "".join(chars)
    print("\nThe decoded message is:", message)
main()