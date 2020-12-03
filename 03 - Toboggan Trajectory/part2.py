#!/usr/bin/env  python3


from functools import reduce
from part1 import load_input
from part1 import find_trees

SLOPS = ((1,1), (3,1), (5,1), (7,1), (1,2))





if __name__ == '__main__':
    grid = load_input()
    print(len(grid))
    print(len(grid[0]))
    num_trees = [ find_trees(grid, dw, dh) for dw, dh in SLOPS ]
    print(num_trees)
    assert num_trees[1] == 211, num_trees[1]
    num_tree = reduce(lambda a, b: a*b, num_trees, 1)

    # 3584591857
    print(f'Answer: {num_tree}')
