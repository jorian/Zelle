__author__ = 'Jorian'
def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "Augustus", "September", "Oktober", "November", "December", ]
        #"JanFebMarAprMayJunJulAugSepOktNovDec"

    #n = eval(input("Enter a month number: "))
    #pos = (n-1) * 3
    #monthAbbrev = months[pos:pos+3]

    #print('the result is:', ord(months[n-1] + "."))

    dateStr = input("Enter a date (mm/dd/yyyy): ")
    monthStr, dayStr, yearStr = dateStr.split("/")

    monthStr = months[int(monthStr)-1]
    print("The converted date is:", monthStr, dayStr+",", yearStr)
main()