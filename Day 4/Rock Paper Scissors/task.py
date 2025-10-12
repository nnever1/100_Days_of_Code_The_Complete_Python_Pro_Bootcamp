import random
from random import randint

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
options=[rock,paper,scissors]
computer_choice = randint(0,2)
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

print(f"You chose {user_choice}")
if user_choice > 2:
    print("Invalid entry")
elif user_choice == 0 and computer_choice == 2:
    print(options[user_choice])
    print(options[computer_choice])
    print("You win computer lose")
elif computer_choice == 0 and user_choice == 2:
    print(options[user_choice])
    print(options[computer_choice])
    print("Computer wins you lose")
elif user_choice > computer_choice:
    print(options[user_choice])
    print(options[computer_choice])
    print("You win. Computer loses")
elif computer_choice > user_choice:
    print(options[user_choice])
    print(options[computer_choice])
    print("You lose. Computer wins")
else:
    print(options[user_choice])
    print(options[computer_choice])
    print("Draw!")