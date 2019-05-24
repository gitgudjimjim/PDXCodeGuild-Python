# guess_the_number.py
import random
num_com = random.randint(1, 10)
in_num = input("guess the number")
in_num = int(in_num)

while True:
    if in_num == num_com:
        print("correct. lucky guess")
        break
    if in_num != num_com:
        print("incorrect. guess again")
        input("guess the number")

turn_number = 0
while in_num != num_com:
    print(f"incorrect, guess again, you have {10-turn_number}")
    in_num = input("guess the number")
    turn_number = turn_number + 1
    if turn_number > 10 and in_num != num_com:
        print("you lose")

turn_number = 0
while in_num != num_com:
    print(f"incorrect, guess again")
            in_num = input("guess the number")
            turn_number = turn_number + 1
if in_num == num_com:
    print(f"you took {turn_number}turns)
    break




    
