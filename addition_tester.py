# addition_tester.py
import random
num1 = random.randint(1, 5)
num2 = random.randint(1, 5)
print(f"{num1} + {num2}")
while True:
    user_answer = input("what is the answer? >")
    user_answer = int(user_answer)
    if user_answer == num1 + num2:
        print("correct!")
        break
    elif user_answer > num1 + num2:
        print("too high")
    elif user_answer < num1 + num2:
        print("too low")
    
