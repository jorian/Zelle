__author__ = 'Jorian'
def happy():
    print("Happy birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ",")
    happy()

def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Henk")
main()