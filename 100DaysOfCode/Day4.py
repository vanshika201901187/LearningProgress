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


choice = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(choice[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(choice[computer_choice])

if user_choice == computer_choice:
  print("It's a draw.")
elif user_choice == 0:             #rock
  if computer_choice == 1:
    print("You lose.")
  elif computer_choice == 2:
    print("You win!")
elif user_choice == 1:             #paper
  if computer_choice == 0:
    print("You win!")
  elif computer_choice == 2:
    print("You lose.")
elif user_choice == 2:             #scissors
  if computer_choice == 0:
    print("You lose.")
  elif computer_choice == 1:
    print("You win!")
