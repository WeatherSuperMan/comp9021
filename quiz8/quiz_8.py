# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randrange

from stack_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

sum_path = 0
path = list()
stack = Stack()
default_direction = 1
dot_set = set()
direction_set = set()
    
def explore_depth_first(x, y, target):
    global sum_path
    global path
    global default_direction
    global dot_set
    global direction_set
    p = x
    q = y

    default_direction = init_dir(p, q)
    stack.push(((p, q), direction_set))
    dot_set.add((p, q))
    sum_path += grid[p][q]
    ##
    ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
    ##print(default_direction)
    ##print(sum_path)
    ##print(dot_set)
    ##
    while not stack.is_empty():
        if sum_path == target:
            while not stack.is_empty():
                path.append((stack.peek()[0][0],stack.peek()[0][1]))
                stack.pop()
            return list(reversed(path))

        if len(dot_set) == 100:
            return

        if sum_path > target:
            if stack.is_empty():
                return path
            i, j = stack.peek()[0]
            stack.pop()
            if stack.is_empty():
                return path
            dot_set.remove((i, j))
            sum_path -= grid[i][j]
            default_direction = max(stack.peek()[1])
        
        p, q = stack.peek()[0]
        next_mov(p ,q, default_direction)

    return path ## no result in the end 

def init_dir(m, n):##init direction and direction_set
    if m > 0:
        return 1
    elif n < 9:
        direction_set.add(1)
        return 2
    elif m < 9:
        direction_set.add(1)
        direction_set.add(2)
        return 3
    elif n > 0:
        return 4
    
def next_mov(a, b, def_dir):##try four directions from default, if neither pop 
    global default_direction
    global direction_set
    direction_set = stack.peek()[1]

    if reachable_direction(a, b, def_dir):
        default_direction = reachable_direction(a, b, def_dir)
        stack.peek()[1].union(direction_set)
        next_dot(a, b, default_direction)
        ##
        ##print('keep going', default_direction)
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        
    elif reachable_direction(a, b, def_dir + 1):
        default_direction = reachable_direction(a, b, def_dir + 1)
        stack.peek()[1].union(direction_set)
        next_dot(a, b, default_direction)
        ##
        ##print('turn1', default_direction)
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        
    elif reachable_direction(a, b, def_dir + 2):
        default_direction = reachable_direction(a, b, def_dir + 2)
        stack.peek()[1].union(direction_set)
        next_dot(a, b, default_direction)
        ##
        ##print('turn2', default_direction)
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        
    elif reachable_direction(a, b, def_dir + 3):
        default_direction = reachable_direction(a, b, def_dir + 3)
        stack.peek()[1].union(direction_set)
        next_dot(a, b, default_direction)
        ##
        ##print('turn3', default_direction)
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        
    else:## cannot continue, pop
        global sum_path
        if stack.is_empty():
            return path
        i, j = stack.peek()[0]
        stack.pop()
        if stack.is_empty():
            return path
        dot_set.remove((a, b))
        sum_path -= grid[a][b]
        def_dir = max(stack.peek()[1])
        ##
        ##print('turn pop')
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        
def reachable_direction(m, n, dire):
    global direction_set
    flag = 0
    if dire > 4:
        ##
        ##print('reset direction')
        ##
        dire -= 4
        
    if dire == 1:
        if m > 0 and (m - 1, n) not in dot_set and dire not in direction_set:
            flag = 1
            return 1
        else:
            direction_set.add(1)

    if dire == 2:
        if n < 9 and (m, n + 1) not in dot_set and dire not in direction_set:
            flag = 1
            return 2
        else:
            direction_set.add(2)

    if dire == 3 and (m + 1, n) not in dot_set and dire not in direction_set:
        if m < 9:
            flag = 1
            return 3
        else:
            direction_set.add(3)

    if dire == 4 and (m, n - 1) not in dot_set and dire not in direction_set:
        if n > 0:
            flag = 1
            return 4
        else:
            direction_set.add(4)

    if flag == 0:
        return False
    
def next_dot(m, n, dire):
    global sum_path
    
    if dire == 1:
        stack.peek()[1].add(1)
        ##
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        m -= 1
        stack.push(((m, n), set()))
        dot_set.add((m, n))
        sum_path += grid[m][n]
        
    elif dire == 2:
        stack.peek()[1].add(2)
        ##
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        n += 1
        stack.push(((m, n), set()))
        dot_set.add((m, n))
        sum_path += grid[m][n]
        
    elif dire == 3:
        stack.peek()[1].add(3)
        ##
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        m += 1
        stack.push(((m, n), set()))
        dot_set.add((m, n))
        sum_path += grid[m][n]
        
    elif dire == 4:
        stack.peek()[1].add(4)
        ##
        ##print((stack.peek()[0][0],stack.peek()[0][1]), stack.peek()[1])
        ##
        n -= 1
        stack.push(((m, n), set()))
        dot_set.add((m, n))
        sum_path += grid[m][n] 
        
    
try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
