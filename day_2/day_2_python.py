# Data Types
print("Hello"[1])
print("Hello"[-1])
# Calculate the BMI
# 🚨 Don't change the code below 👇
print("We'll calculate Your BMI")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
wt = float(weight)
ht = float(height)
bmi = wt / (ht * ht)
# bmi = int(weight) // (int(height) * int(height))
#print(bmi)
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, and you are underweight.")
elif 18.5 < bmi <= 24.9:
    print(f"Your BMI is {bmi}, and You have normal weight.")
elif 24.9 < bmi < 30:
    print(f"Your BMI is {bmi}, and You are overweight.")
else:
    print(f"Your BMI is {bmi}, and You are obese.")

# Calculate life from 90 years in Days, weeks and month
# 🚨 Don't change the code below 👇
print("Your life in week and days left from 90 years")
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
max_age_year = 90
max_age_month = 90 * 12
max_age_week = 90 * 52
max_age_days = 90 * 365
age_num = int(age)
age_year = max_age_year - age_num
age_month = max_age_month - (age_num * 12)
age_week = max_age_week - (age_num * 52)
age_days = max_age_days - (age_num * 365)

print(f"You have {age_days} days, {age_week} weeks, {age_month} months, and {age_year} years left.")

# add the digit of 2 digit number
# 🚨 Don't change the code below 👇
print("Addition of 2 digit number")
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
try:
    digit_number = int(two_digit_number)
    if 9 < digit_number < 100:
        a = digit_number // 10
        b = digit_number % 10
        sum_of_digit = a + b
        print(sum_of_digit)
    else:
        print("Please enter two digit number")
except ValueError:
    print("Entered value is not a number. Please Enter the two digit integer value")


#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")

bill_amount = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
persons = int(input("How many people to split the bill?"))

payment = (bill_amount / persons) * ((100 + tip) / 100)
tip_round = round(payment, 2)
print(f"Each person should pay: ${tip_round}")



