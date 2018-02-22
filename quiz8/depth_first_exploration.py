########################################original version
from stack_adt import *
T = {1 : [2, 4, 5], 2 : [3], 5 : [6, 11, 13], 6 : [7, 8, 10], 8 : [9], 11 : [12]}
def depth_first_exploration():
    stack = Stack()
    stack.push([1])
    while not stack.is_empty():
        path = stack.pop()
        print(path)
        if path[-1] in T:
            for child in reversed(T[path[-1]]):
                stack.push(list(path) + [child])

depth_first_exploration()


########################################defaultdict tree version
from collections import defaultdict
def tree():
    return defaultdict(tree)
T = tree()
T[1][2][3] = None
T[1][4] = None
T[1][5][6][7] = None
T[1][5][6][8][9] = None
T[1][5][11][12] = None
T[1][5][13] = None

def depth_first_exploration_defaultdict():
    stack = Stack()
    stack.push(([1],T[1]))
    while not stack.is_empty():
        path, tree = stack.pop()
        print(path)
        if tree:
            for child in reversed(list(tree)):
                stack.push((list(path) + [child], tree[child]))

depth_first_exploration_defaultdict()
