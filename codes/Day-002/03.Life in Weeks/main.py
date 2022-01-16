# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
left_age = 90 - int(age)
days = left_age * 365
weeks = left_age * 52 
months = left_age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")