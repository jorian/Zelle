__author__ = 'Jorian'

def ticketFinePolicy(speedlimit, clockedspeed):


    if clockedspeed > speedlimit:
        if clockedspeed > 90:
            fine = 5 * (clockedspeed - speedlimit) + 50 + 200
            return fine
        else:
            fine = 5 * (clockedspeed - speedlimit) + 50
            return fine
    else:
        fine = 0
        return fine

def main():
    speedlimit = int(input("Please enter the speed limit for this area: "))
    clockedspeed = int(input("Please enter the clocked speed: "))

    print("You need to pay: €{0:0.2f}".format(ticketFinePolicy(speedlimit, clockedspeed)))

if __name__ == '__main__':
    main()