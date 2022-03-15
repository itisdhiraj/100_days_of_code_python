#Check the eligiblity to ride rollercoaster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
  print("You are allow to Ride. Have fun. ")
else:
  print("Sorry, Your height is less than or equal to 120 cm. You ared not allow to ride.")

#Write a program that works out whether if a given number is an odd or even number.
# 🚨 Don't change the code below 👇
print("Program to check whether given number is an odd or even number.")
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (number % 2 == 0):
    print("This is an even number.")
else:
    print("This is an odd number.")


# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# 🚨 Don't change the code below 👇
print("Welcome to Body Mass Index (BMI) Calculator.")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
wt = float(weight)
ht = float(height)
bmi_round = wt / (ht * ht)
# bmi = int(weight) // (int(height) * int(height))
bmi = round(bmi_round)

#print(bmi)
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")






