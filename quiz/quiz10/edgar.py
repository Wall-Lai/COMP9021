# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree_adt import *

def print_growing_up(tree):
    global L
    if tree.value is None:
        return
    L = []
    for _ in range(tree.height() + 1):
        L.append([])
    _print_growing_up(tree, 0, tree.height())
    __print_growing_up(L, tree.height())

def _print_growing_up(tree, n, height):
    global L
    if n > height:
        return
    if tree.value is None:
        L[n].append(' ')
        _print_growing_up_no_value(n + 1, height)
        _print_growing_up_no_value(n + 1, height)
    else:
        L[n].append(tree.value)
        _print_growing_up(tree.left_node, n + 1, height)
        _print_growing_up(tree.right_node, n + 1, height)

def _print_growing_up_no_value(n, height):
    if n > height:
        return
    L[n].append(' ')
    _print_growing_up_no_value(n + 1, height)
    _print_growing_up_no_value(n + 1, height)
        
def __print_growing_up(L, height):
    for i in range(height, -1, -1):
        string = ''
        for item in L[i]:
            string = string + ' ' * (2 ** (height - i) - 1) + str(item) + ' ' * (2 ** (height - i))
        print(string.rstrip())

try:
    seed_arg, nb_of_nodes = (int(x) for x in
                              input('Enter two integers, with the second one between 0 and 10: '
                                   ).split()
                            )
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
print_growing_up(tree)
#tree.print_binary_tree()