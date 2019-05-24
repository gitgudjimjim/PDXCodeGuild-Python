
import random
user_verbs = input("give me three verbs separated by a comma: >").split(',')

names = input("give me three names separated by a comma: >").split(',')

relatives = input("give me three relatives separated by a comma: >").split(',')


replay = True
while replay:
    yes_inputs = ['yes', 'y']
    no_inputs = ['no', 'n']
    while True:
        hear_story = input("would you like to hear the story? >").lower().strip()
        if hear_story in no_inputs:
            print('valid input')
            replay = False
            break
        elif hear_story in yes_inputs:
            print(user_verbs)
            print(names)
            print(relatives)
            user_verb = random.choice(user_verbs).strip()
            name = random.choice(names).strip()
            relative = random.choice(relatives).strip()
            print(f"hello, my name is {name}. you killed my {relative}. prepare to {user_verb}.")
            hear_another_story = input("would you like to hear another story? >").lower().strip()
            if hear_another_story in no_inputs:
                print('valid input')
                replay = False
                break
            elif hear_another_story in yes_inputs:
                user_verb = random.choice(user_verbs).strip()
                name = random.choice(names).strip()
                relative = random.choice(relatives).strip()
                print(f"hello, my name is {name}. you killed my {relative}. prepare to {user_verb}.")
                input("would you like to hear another story? >").lower().strip()
                if hear_another_story in no_inputs:
                    replay = False
                    break

        else:
            print("please give a yes or no answer")
#            hear_story = input("would you like to hear the story? >").lower().strip()
#            if hear_story in no_inputs:
#                print('valid input')
#                replay = False
#                break
#            elif hear_story in yes_inputs:
#                print(f"hello, my name is {name}. you killed my {relative}. prepare to {user_verb}.")
#                hear_another_story = input("would you like to hear another story? >").lower().strip()
#                if hear_another_story in no_inputs:
#                    print('valid input')
#                    replay = False
#                    break
#                elif hear_another_story in yes_inputs:
#                    print(f"hello, my name is {name}. you killed my {relative}. prepare to {user_verb}.")
#                    if hear_another_story in no_inputs:
#                        replay = False
#                        break
