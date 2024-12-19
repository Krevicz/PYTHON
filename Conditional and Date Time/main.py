numbers = int(input("Enter a number: "))
#even and odd
if numbers % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#positive, negative and zero
if numbers < 0:
    print("The number is negative")
elif numbers == 0:
    print("The number is zero")
else:
    print("The number is positive")
#bmi index
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
number = weight / (height ** 2)
if number < 18.5:
    print("Underweight")
elif number >= 18.5 and number < 24.9:
    print("Normal")
elif number >= 25 and number < 29.9:
    print("Overweight")
elif number >= 30 and number < 34.9:
    print("Obese")
else:
    print("Extremely obese")
#day and time
import datetime
import calendar
print("Time: ", datetime.datetime.now())
print(calendar.calendar(2024))
