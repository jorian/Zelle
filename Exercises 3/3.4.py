__author__ = 'Jorian'
# Calculate the distance between flash and thunder.
def main():
    sec = float(input("How many seconds between flash and thunder? "))
    ft = 1100
    mile = 5280
    distance = sec * ft
    if distance > mile:
        distancemile = distance // mile
        distancefoot = distance % mile
        print("The distance is", distancemile, "mile(s) and", distancefoot, "ft.")
    else:
        print("The distance is", distance, "ft.")
main()