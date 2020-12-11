#!/usr/bin/env  python3


from collections import Counter
from itertools import chain
from part1 import (
        load_input,
        EMPTY,
        OCCUPIED,
        FLOOR,
        )
from pathlib import Path
from typing import (
        Sequence,
        Tuple,
        )



DIRECTIONS = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        )



def look(x: int, y: int, d, data: Tuple[Tuple[str]]):
    """
    What is the first type of sit we see in direction `d`?
    """
    x += d[0]
    y += d[1]
    while 0 <= y < len(data) and 0 <= x < len(data[0]):
        sit = data[y][x]
        if sit != FLOOR:
            return sit
        x += d[0]
        y += d[1]

    return FLOOR



def neighbors_count(x: int, y: int, data: Tuple[Tuple[str]]):
    """
    What are the types of the first sit we see in each of the 8 directions?
    """
    return Counter(look(x, y, d, data) for d in DIRECTIONS)



def iteration(data: Sequence[int]):
    """
    Returns a new floor plan after one iteration of the game.
    """
    width = len(data[0])
    floor = []
    for y, row in enumerate(data):
        new_row = []
        for x, sit in enumerate(row):
            surrounding_sites = neighbors_count(x, y, data)
            #print(x, y, surrounding_sites)
            if sit == EMPTY and surrounding_sites.get(OCCUPIED , 0) == 0:
                new_row.append(OCCUPIED)
            elif sit == OCCUPIED and surrounding_sites.get(OCCUPIED, 0) >= 5:
                new_row.append(EMPTY)
            else:
                new_row.append(sit)
        assert len(new_row) == width, f'{len(new_row)}, {width}'
        floor.append(tuple(new_row))
    assert len(floor) == len(data)

    return tuple(floor)



def solve(data: Sequence[int]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    while True:
        floor = iteration(data)
        #print(*floor, sep='\n', end='\n\n')
        print('.', end='')
        if all(f == d for f, d in zip(floor, data)):
            return Counter(chain.from_iterable(floor))[OCCUPIED]
        data = floor





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 2032
    print(f'Answer: {answer}')
