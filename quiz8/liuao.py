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

def explore_depth_first(x, y, target):
    # [x,y,up,down,left,right]
    # dir : up = 2 down = 3 left = 4 right = 5
    '''
    mxsum = 0
    for row in grid:
        for ex in row:
            mxsum+=ex
    if mxsum < target:
        return None
    '''
    stk = Stack()
    dir = 1
    sum = 0
    st = set()
    i = 0
    while True:
        while x>= 0 and x<10 and y>= 0 and y <10 and sum<target and (x,y) not in st:
            stk.push((x,y))
            st.add((x,y))
            sum += grid[x][y]
            #print((x,y),'---',grid[x][y] ,'---' , sum )
            #print(stk._data)
            if sum<target:
                x,y = move(x,y,dir)
        if sum == target:
            lst = []
            while not stk.is_empty():
                lst.append((stk.peek()[0],stk.peek()[1]))
            #lst.append(stk.peek())
                stk.pop()
            return list(reversed(lst))
        # sum > target or out bound, trace back
        if len(st) == 100:
            return None
        backtrack = False
        if sum > target:
            #print('entered')
            sum -= grid[x][y]
            stk.pop()
            st.remove((x,y))
            x = stk.peek()[0]
            y = stk.peek()[1]
            backtrack = True
            #stk.pop()
            #st.remove((x,y))
        else:
            x = stk.peek()[0]
            y = stk.peek()[1]
        # change direction
        poppedTuple = []
        while not explorable(x,y,sum,target,st):
            #print('--x y---',x,y)
            #print('value ' , grid[x][y])
            #print('--sum--', sum)
            backtrack = True
            s = stk.pop()
            #print(s)
            poppedTuple.append(s)
            sum-=grid[x][y]
            if not stk.is_empty():
                x = stk.peek()[0]
                y = stk.peek()[1]
                #print('peek is ', stk.peek())
            else:
                #print(len(st))
                return None
        for e in poppedTuple:
            st.remove(e)
        if backtrack:
            dir = getDir(x,y,dir,sum,target,st)
        else: dir = chdir(dir)
        x,y = move(x,y,dir)    
        if stk.is_empty():
            return None


def getDir(x,y,dir,sum,target,st):
    d = dir
    d = chdir(d)
    i, j = move(x,y,d)
    sm = sum+grid[i][j]
    count = 0 
    while (i not in range(0,9) or j not in range(0,9) or sm > target or (i,j) in st) and count<4:
        count+=1
        d = chdir(d)
        sm -= grid[i][j]
        i, j = move(x,y,d)
        sm += grid[i][j]
    if d!= dir: dir = d
    return dir

        

def explorable(x,y , sum ,target, st):
    #print(x,y)
    if x > 0:
        if (x-1,y) not in st and grid[x-1][y] + sum <= target:
            #print('===flag a')
            return True
    if y > 0:
        if (x,y-1) not in st and grid[x][y-1] + sum <= target:
            #print('===flag b')
            return True
    if x < 9:
        if (x+1,y) not in st and grid[x+1][y] + sum <= target:
            #print('===flag c')
            return True
    if y < 9:
        if (x,y+1) not in st and grid[x][y+1] + sum <= target:
            #print('===flag d')
            return True
    return False

def move(x,y,dir):
    if dir == 1:
        x-=1
    if dir == 2:
        y+=1
    if dir == 3:
        x+=1
    if dir == 4:
        y-=1
    return x,y

def chdir(d):
    if d < 4:
        d+=1
    else: d = 1
    return d




    # Replace pass above with your code


try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
st = set()
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
