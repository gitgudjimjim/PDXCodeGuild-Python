# enough_sleep.py
user_sleep = input("how much did you sleep last night? >")
user_sleep = int(user_sleep)
if user_sleep < 6:
        print("sleep more!")
if user_sleep > 11:
        print("sleep less!")
if user_sleep >=6 and user_sleep <=11:
        print("great job!")
