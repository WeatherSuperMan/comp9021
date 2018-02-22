import sys
from collections import deque

##input initial state
try:
    number_list = []
    number_sting = input('Input final configuration: ')
    for c in number_sting:
        if c.isspace():
            pass
        elif c.isdigit():
            number_list.append(c)
        else:
            raise ValueError
except ValueError:
    print('Incorrect configuration, giving up...')
    sys.exit()
try:
    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])
    standard_list = [1, 2, 3, 4, 5, 6, 7, 8]
    if sorted(number_list) != standard_list:
        raise ValueError
except ValueError:
    print('Incorrect configuration, giving up...')
    sys.exit()

##define dict
init = [1, 2, 3, 4, 5, 6, 7, 8]
final = tuple(number_list)

#define transformations
def row_exchange(S):
    s = list(S)
    s[0] = S[7]
    s[1] = S[6]
    s[2] = S[5]
    s[3] = S[4]
    s[4] = S[3]
    s[5] = S[2]
    s[6] = S[1]
    s[7] = S[0]
    return  s

def right_circular_shift(S):
    s = list(S)
    s[0] = S[3]
    s[1] = S[0]
    s[2] = S[1]
    s[3] = S[2]
    s[4] = S[5]
    s[5] = S[6]
    s[6] = S[7]
    s[7] = S[4]
    return  s

def middle_clockwise_rotation(S):
    s = list(S)
    s[1] = S[6]
    s[2] = S[1]
    s[5] = S[2]
    s[6] = S[5]
    return  s

##main
process = deque([])
stored = set({})
step = 0
process.append([tuple(init),0])

while True:
    if process[0][0] == final:
        step = process[0][1]
        break
    else:
        stored.add(process[0][0])
        if tuple(row_exchange(list(process[0][0]))) not in stored:
            process.append([tuple(row_exchange(list(process[0][0]))),process[0][1] + 1])
        if tuple(right_circular_shift(list(process[0][0]))) not in stored:
            process.append([tuple(right_circular_shift(list(process[0][0]))),process[0][1] + 1])
        if tuple(middle_clockwise_rotation(list(process[0][0]))) not in stored:
            process.append([tuple(middle_clockwise_rotation(list(process[0][0]))),process[0][1] + 1])
        process.popleft()

##output steps
if step == 0 or step == 1:
    print(step,'step is needed to reach the final configuration.')
else:
    print(step,'steps are needed to reach the final configuration.')
