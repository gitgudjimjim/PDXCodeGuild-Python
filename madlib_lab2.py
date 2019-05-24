
import random
user_verbs = input("give me three verbs separated by a comma: >")
user_verbs = user_verbs.split(', ')
random.choice(user_verbs)
user_verbs = random.choice(user_verbs)
name = input("give me a name >")
relative = input("give me a relative >")

replay = True
while replay:
    yes_inputs = ['yes', 'y']
    no_inputs = ['no', 'n']
    while True:
        hear_story = input("would you like to hear the story? >").lower().strip()
        if hear_story in yes_inputs + no_inputs:
            print('valid input')
            break
        else:
            print("please give a yes or no answer")
    if hear_story in no_inputs:
            replay = False
    else:
        print(f"hello, my name is {name}. you killed my {relative}. prepare to {user_verbs}.")
