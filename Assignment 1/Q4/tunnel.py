import os.path
import sys
import re
from collections import deque


filename = input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(filename):
    print(f'Sorry, input file does not store valid data.')
    sys.exit()
#read file
result = []
a_l = []
L=[]
with open(filename,'r') as f:
    result=f.readlines()
#arrange file to list
for i in result:
    L.append(re.findall(r'\d+',i))
for i in L:
    if i != []:
        a_l.append(list(map(int, i)))
#distance from west
ceil = a_l[0]
floor = a_l[1]
num_c = 0
num_f = 0
for i in ceil:
    if i > floor[0]:
        num_c += 1
    else:
        break
for i in floor:
    if i < ceil[0]:
        num_f += 1
    else:
        break
distance_from_west = min(num_c,num_f)
print(f'From the west, one can see into the tunnel over a distance of {distance_from_west}.')
#Q2
distance_L = []
for i in range(0,len(ceil)):
    count_ceil = 0
    count_floor = 0
    for j in range(i + 1, len(ceil)):
        if ceil[i] >= ceil[j]:
            break
        else:            
            if ceil[i] < floor[j]:
                if ceil[i+1] > floor[j]:
                    ceil[i] = ceil[j]
                    count_ceil += 1
                else:
                    break
            else:
                count_ceil += 1
    distance_L.append(count_ceil)
    for j in range(i + 1, len(ceil)):
        if floor[i] <= floor[j]:
            break
        else:
            if floor[i] > ceil[j]:
                if floor[i+1] < ceil[j]:
                    floor[i] = ceil[j]
                    count_floor += 1
                else:
                    break
            else:
                count_floor += 1
    distance_L.append(count_floor)
distance = max(distance_L)
print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {distance}.')
