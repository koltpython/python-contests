# Author: mtasci18
weight = float(input())
height = float(input())

BMI = weight/height**2

if BMI < 18.5:
    print('Underweight')
elif 18.5 <= BMI <= 24.9:
    print('Healthy Weight')
elif 25 <= BMI <= 29.9:
    print('Overweight')
elif 30 <= BMI <= 34.9:
    print('Obese')
elif 35 <= BMI <= 39.9:
    print('Severely Obese')
elif 40 <= BMI:
    print('Morbidly Obese')