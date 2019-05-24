# rps.py
import random

def calc_winner(comp_choice, user_choice):
  defeats = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
  }

  comp_choice = 'paper'
  user_choice = 'scissors'

  if comp_choice == user_choice:
    return 'Tie'
  elif defeats[comp_choice] == user_choice:
    return 'computer wins'
  else: #elif defeats[comp_choice] != user_choice
    return 'User wins'

rps = ['rock', 'paper', 'scissors']
while True:
    user_choice = input('rock, paper, or scissors: ').strip().lower()
    if user_choice not in rps:
        break
    print('please choose rock, paper, or scissors')

computer_choice = random.choice(rps)
print(computer_choice)
print(calc_winner(computer_choice, user_choice))
