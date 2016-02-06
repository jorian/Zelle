__author__ = 'Jorian'


def valueName(name):
    totalname = "".join(name.split())

    value = 0
    for ch in totalname:
        value = value + ord(ch.lower()) - ord('a') + 1
    return value
def main():
    name = input("Please enter your name: ")
    print("The value of your name", name, "is:", valueName(name))


main()
