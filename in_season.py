# in_season.py
import random
ingredient_list = ['tomatoes' , 'cucumber']
food_list = ['pizza' , 'cucumber soup']
user_food = input(f"what would you like to make, {food_list[0]} or {food_list[1]}?")
while user_food not in food_list:
    user_food = input(f"what would you like to make, {food_list[0]} or {food_list[1]}?")
in_season = random.choice(ingredient_list)
print(f"{in_season} are in season")
if in_season == 'tomatoes':
    if user_food == 'pizza':
        print("go for it!")
    else:
        print("I hope you like cucumber pizza")
else:
    if user_food == 'cucumber soup':
        print("have fun with that cucumber soup!")
    else:
        print("looks like you have to make pizza!")
