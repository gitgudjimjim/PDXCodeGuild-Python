# guess_the_vowel.py
import random

vowel_string = 'aeiou'
chosen_vowel = random.choice(vowel_string)
user_input = input("what vowel am i thinking of?")
if user_input == chosen_vowel:
    print("you're a genius!")
turn_number = 0
while user_input != chosen_vowel:
    print(f"guess again, you have {3-turn_number}")
    user_input = input("what vowel am i thinking of? >")
    turn_number = turn_number + 1
    if turn_number == 3 and user_vowel != chosen_vowel:
        print("you failed, take it personally")
        break
if user_input == chosen_vowel:
        print("you're a genius!")
