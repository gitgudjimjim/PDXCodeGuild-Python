# rock_paper_scissors.py
import random
choosing = ['rock' , 'paper' , 'scissors']
user_input = input(f"what is your option?")
computer_decision = random.choice(choosing)
if input == 'rock':
    if computer_decision == 'rock':
        print("tie")
    if computer_decision == 'paper':
        print("computer wins")
    if computer_decision == 'scissors':
        print("you win")
if input == 'paper':
    if computer_decision == 'rock':
        print("you win")
    if computer_decision == 'paper':
        print("tie")
    if computer_decision == 'scissors':
        print("computer wins")
if input == 'scissors':
    if computer_decision == 'rock':
        print("computer wins")
    if computer_decision == 'paper':
        print("you win")
    if computer_decision == 'scissors':
        print("tie")
