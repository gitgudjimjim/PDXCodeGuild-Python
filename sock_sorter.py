# sock_sorter.py
import random
sock_list = []
sock_types = ['ankle', 'crew', 'calf', 'thigh']
colors = ['black', 'white', 'blue']
sock_counter = {}
for i in range(100):
    sock = random.choice(sock_types)
    color = random.choice(colors)
    sock_list.append((sock, color))
    sock_counter[sock] = sock_counter.get(((sock, color)), 0) + 1
#if key exists in dict then nothing added, if not then one is created
    # equivalent to above
    # if sock in sock_counter:
    #   sock_counter[sock] += 1
    # else:
    #   sock_counter[sock] = 1
print(sock_list)
print(sock_counter)

for sock in sock_counter:
    print(f'{sock} has {sock_counter.get(sock)%2} loner(s)')

#built in function
#from collections import counter
#counter = counter(sock_list)
#print(counter)
