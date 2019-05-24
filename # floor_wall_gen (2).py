# floor_wallgen.py
import random
floor_wall_list = ['I', '_']
out_string = ''
random_item = random.choice(floor_wall_list)
for piece in range(0, 4):
    out_string = out_string + random.choice(floor_wall_list)
print(out_string)
    
