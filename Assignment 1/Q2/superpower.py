import sys
list_h = []
heroes = []
try:
    list_h = input('Please input the heroes\' powers').split()
    for i in range(0,len(list_h)):
        heroes.append(int(list_h[i]))
    print(heroes)
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
try:
    nb_of_switches = input('Please input the number of power flips:')
    nb_of_switches = int(nb_of_switches)
    print(nb_of_switches)
    if nb_of_switches < 0 or len(list_h)< nb_of_switches:
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
#for Q1
heroes1 = []
heroes1 = sorted(heroes)
nb_of_switches1 = nb_of_switches 
i = 0
remainder = 0
for i in range(0, len(heroes1)):
    if heroes1[i] < 0:
        if nb_of_switches1 > 1:
            heroes1[i] = heroes1[i] * (-1)
            nb_of_switches1 -= 1
        remainder = nb_of_switches1 % 2
heroes1 = sorted(heroes1)
if remainder == 1:
    heroes1[0] = heroes1[0] * (-1)
max1 = sum(heroes1)
#for Q2
heroes2 = []
heroes2 = sorted(heroes)
i = 0
for i in range(0, nb_of_switches):
    heroes2[i] =  heroes2[i] * (-1)
max2 = sum(heroes2)

# for Q3
sum_s = 0
sum_l = []
for i in range(0, len(heroes)-nb_of_switches+1):
    sum_s = sum(heroes[i:i+nb_of_switches])
    sum_l.append(sum_s)
max3 = sum(heroes) - min(sum_l)*2  
#for Q4
heroes4 = []
for i in heroes:
    heroes4.append(i)
l4 = [0]
while(True):
    if len(heroes4) == 0:
        break
    else:
        i = 0
        while i < len(heroes4):
            if heroes4[i] < 0:
                break
            else:
                heroes4.remove(heroes4[i])

        removel= []
        i = 0
        while i < len(heroes4):
            s = sum(heroes4[0:i+1])
            if s <= 0:
                l4.append(s)
                removel.append(heroes4[i])
                i += 1 
            else:
                break
        for i in removel:
            heroes4.remove(i)

max4 = sum(heroes) - min(l4)*2    
#print out
print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {max1}.')
print(f'Flipping the power of the same hero at most once, the greatest achievable power is {max2}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {max3}.')
print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {max4}.')



    
