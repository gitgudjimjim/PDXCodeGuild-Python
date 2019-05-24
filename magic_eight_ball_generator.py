# magic_eight_ball_generator.py
import random
print("welcome to the magic eight ball generator")
print("ask the computer if you will win the lottery tomorrow")
user_answer = input()
computer_answers = ['yes', 'no', 'maybe']
random_com = random.choice(computer_answers)
print(random_com)

while computer_answers == ('yes', 'no', 'maybe'):
    print('ask me another question')
    user_answer = input()

    if user_answer == ('done'):
        break
