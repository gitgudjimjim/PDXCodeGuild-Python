# Password_Generator.py
in_num = input("how many characters do you want your password to be?")
in_num = int(in_num)
import random
import string
print(in_letter * in_num)
out_string = ''
for num in range(0, in_num):
    out_string = out_string +
in_letter = random.choice(string.ascii_lowercase)
counter = 0
while True:
    counter = counter + 1
    if counter == 0:
        print(random.choice(string.ascii_lowercase))
    if counter == 1:
        print(random.choice(string.ascii_lowercase))
    if counter == 2:
        print(random.choice(string.ascii_lowercase))
    if counter == 3:
        print(random.choice(string.ascii_lowercase))
    if counter == 4:
        print(random.choice(string.punctuation))
    if counter == 5:
        print(random.choice(string.punctuation))
    if counter == 6:
        print(random.choice(string.punctuation))
    if counter == 7:
        break
print(out_string)
