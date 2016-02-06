__author__ = 'Jorian'
def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    y = float(input("Enter a number between 0 and 1: "))
    n = int(input("How many numbers should I print? "))
    print("{0:^5}  {1:^8.8}  {2:^8.8}".format("index", x, y))
    print("-------------------------")
    for i in range(n):
        x = 3.9 * x * (1.0 - x)
        y = 3.9 * y * (1.0 - y)
        #print("{0:^5}".format(i+1), end="  ")
        print("{0:^5}  {1:6.6f}  {2:6.6f}".format((i+1), x, y))
        #print("{0:6.6f}".format(y))


main()