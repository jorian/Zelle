__author__ = 'Jorian'

def bmiIndicator():
    length = float(input("Please enter your length in centimeters: "))
    weight = float(input("Please enter your weight in kilograms: "))

    bmi = (weight / ((length / 100) ** 2))
    if bmi < 18.5:
        situation = "below"
    elif 18.5 <= bmi < 25:
        situation = "within"
    elif 25 <= bmi < 30:
        situation = "just above"
    elif 30 <= bmi < 40:
        situation = "above"
    elif bmi > 40:
        situation = "heavily above"
    print("Your BMI is:", bmi,'\n')
    print("This is", situation, "the healthy range.")
if __name__ == '__main__':
    bmiIndicator()