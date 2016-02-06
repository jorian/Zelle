__author__ = 'Jorian'
def main():

    infileName = "C:/Users/Jorian/Desktop/henk.py"
    outfileName = "C:/Users/Jorian/Desktop/henkie.py"


    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    lines = []
    for line in infile:
        first, last = line.split()
        uname = (first[0]+last[:7]).upper()
        print(uname, file=outfile)

    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

    outfileNew = open(outfileName, "r")
    for line in outfileNew:
        print(line)

    outfile.close()
    #first = input("Please enter your first name in lowercase letters: ")
    #last = input("Please enter your last name in lowercase letters: ")

    #uname = first[0] + last[:7]

    #print("Your username is", uname)
main()