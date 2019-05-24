import random
eyes = ['=' , ':' , ';']
noses = ['<' , '>' , '-']
mouths = ['o' ,'[' , ']']
random_eyes = random.choice(eyes)
random_nose = random.choice(nose)
random_mouth = random.choice(mouth)
for piece in range (0, 1):
out_string = out_string + random.choice(eyes) + random.choice(nose) + random.choice(mouth)
print(out_string)
