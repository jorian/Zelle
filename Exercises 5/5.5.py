__author__ = 'Jorian'


def valuename():
    name = input("Please enter your name:")
    totalname = "".join(name.split())

    print(totalname)

    value = 0
    for ch in totalname:
        value = value + ord(ch.lower()) - ord('a') + 1

    print("The value is:", value)


valuename()
