
import random
user_verbs = input("give me three verbs separated by a comma: >")
user_verbs = random.choice(user_verbs.split(', '))
names = input("give me three names separated by a comma: >")
names = random.choice(names.split(', '))
relatives = input("give me three relatives separated by a comma: >")
relatives = random.choice(relatives.split(', '))

replay = True
while replay:
    yes_inputs = ['yes', 'y']
    no_inputs = ['no', 'n']
    while True:
        hear_story = input("would you like to hear the story? >").lower().strip()
        if hear_story in no_inputs:
            print('valid input')
            input("would you like to hear another story? >")
            if hear_story in no_inputs:
                break
            elif hear_stor
        elif hear_story in yes_inputs:
            print(f"hello, my name is {name}. you killed my {relative}. prepare to {user_verbs}.")
        else:
            print("please give a yes or no answer")
            input("would you like to hear another story? >")
            if input() in no_inputs:
                break
            elif input() in yes_inputs:
                print(f"hello, my name is {names}. you killed my {relatives}. prepare to {user_verbs}.")
            else:
                print("please give a yes or no answer")
    else:
        print(f"hello, my name is {names}. you killed my {relatives}. prepare to {user_verbs}.")
