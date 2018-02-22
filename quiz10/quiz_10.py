# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample

from priority_queue_adt import *


# Possibly define some functions

def preferred_sequence():

    preferred_list = list()

    for k in range(length):
        que_list = list(pq._data)
        que_comp = list(que_list[ : len(pq) + 1])
        que_length = int(pq._length)

        max_del_e = min(pq._data[1:len(pq) + 1])
        max_del_e_index = 0
        
        for j in range(1, len(pq) + 1):## select largest element which can be delete

            del_e = delete_element(j)
            pq.insert(del_e)
            
            if pq._data[ : len(pq) + 1] == que_comp:
                if del_e >= max_del_e:
                    max_del_e = del_e
                    max_del_e_index = j
                    
            pq._data = list(que_list)
            pq._length = int(que_length)

        preferred_list.append(max_del_e)
        delete_element(max_del_e_index)
        
    preferred_list.reverse()
    return(preferred_list)

def delete_element(i):
    max_element = pq._data[i]
    pq._data[i], pq._data[pq._length] = pq._data[pq._length], pq._data[i]
    pq._length -= 1
    pq._bubble_down(i)
    return max_element


try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())
