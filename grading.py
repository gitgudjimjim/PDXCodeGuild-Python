# grading.py
valid_inputs = ['yes', 'y', 'no', 'n']
while True:
    grade = input('what letter grade does my number grade equal? what is your number grade?')
    grade = int(grade)
    ones_digit = grade % 10
    if grade >= 90:
            letter_grade = ('A')
    if grade >=80 and grade <=89:
            letter_grade = ('B')
    if grade >= 70 and grade <=79:
            letter_grade = ('C')
    if grade >= 60 and grade <=69:
            letter_grade = ('D')
    if grade >= 0 and grade <=59:
            letter_grade = ('F')
    sign = ''
    if letter_grade != 'F':
        if ones_digit <= 4:
            sign = '-'
        if ones_digit >= 7:
            sign = '+'
    if letter_grade == 'A':
        if grade >= 100:
            sign = '+'
    print(str(letter_grade) + sign)

    valid_inputs = ['yes', 'y', 'no', 'n']
    while True: #input validation
        play_again = input('Do you want to continue?:').strip().lower()
        if play_again in valid_inputs:
            break
    if play_again.startswith('n'): # break out of infinite loop
        print('goodbye!')
        break
    #elif play_again in valid_inputs and play_again.startswith('y'):
        print('in here')
        pass
