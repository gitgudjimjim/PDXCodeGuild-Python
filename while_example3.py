# while_example3.py
counter = 0
while True:
  counter = counter + 1
  if counter % 2 == 0:
    print('a')
  if counter > 4:
    print('b')
  if counter == 7:
    break
