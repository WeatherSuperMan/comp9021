# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

#my code

#remove repeated elements and sort
M = sorted(list(set(L)))
N = []

#remove 0, add ['0',0] to N, N combines ['a/b',a/b]
if M[0] == 0:
    M.pop(0)
    N.append(['0',0])
len_M = len(M)
#print('\n',M)
#print(len_M)

#generate and sort N
for i in range(1, len_M):
    for j in range(i):
        z = int(M[j]/gcd(M[i],M[j]))
        m = int(M[i]/gcd(M[i],M[j]))
        if [f'{z}/{m}',M[j]/M[i]] not in N:
            N.append([f'{z}/{m}',M[j]/M[i]])
N.append(['1',1])
N = sorted(N, key = lambda N : N[1])
#print(N)

#generate fractions
for i in range(len(N)):
    fractions.append(N[i][0])

#generate closest number
if '1/2' in fractions:
    spot_on = True
else:
    if N[0][1] > .5:
        closest_1 = N[0][0]
    if N[0][1] < .5:
        for i in range(len(N)):
            if N[i][1] < .5:
                pass
            if N[i][1] > .5:
                c_1 = N[i-1][1]
                c_2 = N[i][1]
                if abs(c_1 - .5) == abs(c_2 - .5):
                    closest_1 = N[i-1][0]
                    closest_2 = N[i][0]
                elif abs(c_1 - .5) < abs(c_2 - .5):
                    closest_1 = N[i-1][0]
                else:
                    closest_1 = N[i][0]
                break
#my code

print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
