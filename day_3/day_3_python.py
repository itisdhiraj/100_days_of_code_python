#Check the eligiblity to ride rollercoaster
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))
if height > 120:
  print("You are allow to Ride. Have fun. ")
  age = int(input("Enter the age : "))
  if age <= 12:
    print("You have to pay 5$")
  elif 12 < age < 18:
    print("You have to pay 7$")
  else:
    print("You have to pay 12$")
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

# program that works out whether if a given year is a leap year
# 🚨 Don't change the code below 👇
print("To Check if a given year is a leap year")
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 100 == 0 and year % 400 != 0:
    print("Not Leap year.")
elif year % 400 == 0 or year % 4 == 0:
    print("Leap year.")
else:
    print("Not leap year.")


# build an automatic pizza order program.
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_Pizza = 15
medium_Pizza = 20
large_Pizza = 25
pepperoni_small = 2
pepperoni_other = 3
ext_cheese = 1

if size == "S" or size.lower() == "s":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            amount = small_Pizza + pepperoni_small + ext_cheese
            print(f"Your final bill is: ${amount}.")
        elif extra_cheese == "N":
            amount = small_Pizza + pepperoni_small
            print(f"Your final bill is: ${amount}.")
        else:
            print("Enter Correct input for Cheese.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            amount = small_Pizza + ext_cheese
            print(f"Your final bill is: ${amount}.")
        elif extra_cheese == "N":
            amount = small_Pizza
            print(f"Your final bill is: ${amount}.")
        else:
            print("Enter Correct input for Cheese.")
    else:
        print("Please enter Correct Input for pepperoni. ")

elif size == "M" or size.lower() == "m":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            amount = medium_Pizza + pepperoni_other + ext_cheese
            print(f"Your final bill is: ${amount}.")
        elif extra_cheese == "N":
            amount = medium_Pizza + pepperoni_other
            print(f"Your final bill is: ${amount}.")
        else:
            print("Enter Correct input for Cheese.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            amount = medium_Pizza + ext_cheese
            print(f"Your final bill is: ${amount}.")
        elif extra_cheese == "N":
            amount = medium_Pizza
            print(f"Your final bill is: ${amount}.")
        else:
            print("Enter Correct input for Cheese.")
    else:
        print("Please enter Correct Input for pepperoni. ")
elif size == "L" or size.lower() == "l":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            amount = large_Pizza + pepperoni_other + ext_cheese
            print(f"Your final bill is: ${amount}.")
        elif extra_cheese == "N":
            amount = large_Pizza + pepperoni_other
            print(f"Your final bill is: ${amount}.")
        else:
            print("Enter Correct input for Cheese.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            amount = large_Pizza + ext_cheese
            print(f"Your final bill is: ${amount}.")
        elif extra_cheese == "N":
            amount = large_Pizza
            print(f"Your final bill is: ${amount}.")
        else:
            print("Enter Correct input for Cheese.")
    else:
        print("Please enter Correct Input for pepperoni. ")
else:
    print("Please enter correct input.")
