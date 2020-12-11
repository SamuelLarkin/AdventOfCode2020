#!/usr/bin/env  python3

from collections import Counter
from enum import Enum
from itertools import chain
from pathlib import Path
from typing import (
        Iterable,
        Sequence,
        Tuple
        )


#class PositionType(Enum):
FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def parse_input(lines: Iterable) -> int:
    """
    Convert one line of the puzzle's data.
    """
    return tuple(tuple(line.strip()) for line in lines)


def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def neighbors(x: int, y: int, data: Tuple[Tuple[str]]):
    """
    Yields the immediate neighbors coordinates.
    """
    for yy in range(max(y-1, 0), min(y+2, len(data))):
        for xx in range(max(x-1, 0), min(x+2, len(data[y]))):
            if xx == x and yy == y:
                continue
            yield xx, yy


def neighbors_count(x: int, y: int, data: Tuple[Tuple[str]]):
    """
    Count the neighbors type of sits aka OCCUPIED, EMPTY, FLOOR.
    """
    return Counter(data[yy][xx] for xx,yy in neighbors(x, y, data))


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
            elif sit == OCCUPIED and surrounding_sites.get(OCCUPIED, 0) >= 4:
                new_row.append(EMPTY)
            else:
                new_row.append(sit)
        assert len(new_row) == width, f'{len(new_row)}, {width}'
        floor.append(tuple(new_row))
    assert len(floor) == len(data)

    return tuple(floor)


def solve(data: Sequence[int]) -> int:
    """
    Solve part 1 of the puzzle.
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
    print(len(data), len(data[0]))
    print(*data, sep='\n', end='\n\n')
    #print(list(neighbors(0, 0, data)))
    #print(list(neighbors(len(data[0])-1, 0, data)))

    answer = solve(data)

    # 2222
    print(f'Answer: {answer}')
