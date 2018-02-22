# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children, and
# - the sum of the nodes along all of T*'s branches is equal to M.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)

lmax = 0
rmax = 0
sum_path = 0

def expand_tree(tree):
    m = maxsum(tree)
    node = tree
    next_node_set = set()
    path = list()
    sum_path = 0
    if not node.value:
        return tree
    
    if node.left_node.value:
        next_node_set.add(1)
    if node.right_node.value:
        next_node_set.add(2)

    path.append((node, next_node_set))
    sum_path += node.value
    
    while path:
        next_node_set = set()

        if node.left_node.value and not node.right_node.value and m != sum_path:
            node.right_node = BinaryTree(m - sum_path)
        elif node.right_node.value and not node.left_node.value and m != sum_path:
            node.left_node = BinaryTree(m - sum_path)
        elif not node.left_node.value and not node.right_node.value and m != sum_path:
            node.right_node = BinaryTree(m - sum_path)
            node.left_node = BinaryTree(m - sum_path)

            
        if 1 in path[-1][1]:##left path exist
            path[-1][1].remove(1)
            node = node.left_node
            if node.left_node.value:
                next_node_set.add(1)
            if node.right_node.value:
                next_node_set.add(2)

            path.append((node, next_node_set))
            sum_path += node.value

        elif 2 in path[-1][1]:##right path exist
            path[-1][1].remove(2)
            node = node.right_node
            if node.left_node.value:
                next_node_set.add(1)
            if node.right_node.value:
                next_node_set.add(2)

            path.append((node, next_node_set))
            sum_path += node.value

        else:##neither left or right path exist
            sum_path -= node.value
            path.pop()
            if not path:
                return 
            node = path[-1][0]

            
                    
            
        
def maxsum(tree):
    if not tree.value:
        return 0
    lmax = maxsum(tree.left_node)
    rmax = maxsum(tree.right_node)
    return tree.value + max(lmax, rmax)

                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()



