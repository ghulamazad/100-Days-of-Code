# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1.lower() + name2.lower()

true_total = names.count('t')+names.count('r')+names.count('u')+names.count('e')

love_total = names.count('l')+names.count('o')+names.count('v')+names.count('e')

love_score = true_total * 10 + love_total

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")