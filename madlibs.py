# lab2_madlibs
import random
food1 = input("give me first food >")
food2 = input("give me second food >")
food3 = input("give me third food >")
foodlist = ['food1','food2', 'food3']
foodlistr = random.choice(foodlist)
verb1 = input("give me first way you like to cook your food? >")
verb2 = input("give me second way you like to cook your food? >")
verb3 = input("give me a third way you like to cook your food? >")
verblist = ['verb1', 'verb2', 'verb3']
verblist.split('')
verblistr = random.choice(verblist)
print(f"Hello i like to {verblistr}")
