import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choose = random.randint(0,2)

game_images = [rock,paper, scissors] 

print(game_images[user_choice])
print("Computer choose:")
print(game_images[computer_choose])

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choose == 2:
    print(rock)
    print("You wins!")
elif computer_choose ==0 and user_choice == 2:
    print("You lose")
elif  computer_choose > user_choice:
    print("You lose")
elif user_choice > computer_choose:
    print("You win!")
elif computer_choose == user_choice:
    print("It's a draw")