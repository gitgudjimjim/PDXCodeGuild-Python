# letter_multiplier.py

in_letter = input("what letter would you like to multiply? >")
in_num = input("how many would you like? >")
in_num = int(in_num)
print(in_letter * in_num)
out_string = ''
for num in range(0, in_num):
    out_string = out_string + in_letter
print(out_string)
