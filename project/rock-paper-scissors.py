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

print("Welcome to Augustine's game of Rock-Paper-Scissors\n")

respondent = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors\n"))

import random

computer_response = random.randint(0,2)

#respondent answer and results

if respondent == 0:
  print("Rock\n")
  print(rock)
elif respondent == 1:
  print("Paper\n")
  print(paper)
else:
  print("Scissors\n")
  print(scissors)

#computer response and results

if computer_response == 0:
  print("Rock\n")
  print(rock)
elif computer_response == 1:
  print("Paper\n")
  print(paper)
else:
  print("Scissors\n")
  print(scissors)

#rules

if respondent == computer_response:
  print("It's a tie!")
elif respondent == 0 and computer_response == 1:
  print("You lose!")
elif respondent == 0 and computer_response == 2:
  print("You win!")
elif respondent == 1 and computer_response == 0:
  print("You win!")
elif respondent == 1 and computer_response == 2:
  print("You lose!")
elif respondent == 2 and computer_response == 0:
  print("You lose!")
elif respondent == 2 and computer_response == 1:
  print("You win!")
else:
  print("You typed an invalid number, you lose!")
