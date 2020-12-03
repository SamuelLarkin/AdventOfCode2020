#!/usr/bin/env  python3


def load_input():
    """
    """
    with open('input', 'r') as f:
        grid = tuple( tuple(l) for l in map(str.strip, f) )

    assert len(grid) == 323
    assert all( len(l) for l in grid )

    return grid


def find_trees(grid, dw: int, dh: int) -> int:
    """
    """
    height = len(grid)
    width = len(grid[0])

    num_tree = 0
    # The map is periodic
    for w, h in zip(range(0, int(1e10), dw), range(0, height, dh)):
        w %= width
        #print(w, h)
        #print(grid[h][w])
        if grid[h][w] == '#':
            num_tree += 1

    return num_tree





if __name__ == '__main__':
    grid = load_input()
    print(len(grid))
    print(len(grid[0]))
    num_tree = find_trees(grid, 3, 1)

    # 211
    print(f'Answer: {num_tree}')
