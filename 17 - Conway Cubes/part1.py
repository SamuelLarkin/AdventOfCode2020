#!/usr/bin/env  python3

from enum import Enum
from itertools import (
        chain,
        product,
        )
from pathlib import Path
from typing import (
        Iterable,
        Sequence,
        Set,
        Tuple,
        Union,
        )



Coordinate3D = Tuple[int, int, int]
Coordinate4D = Tuple[int, int, int, int]
Coordinate = Union[Coordinate3D, Coordinate4D]



class State(Enum):
    Active = '#'
    Inactive = '.'



def parse_input(lines: Iterable) -> Set[Coordinate]:
    """
    Convert one line of the puzzle's data.
    """
    grid: Set[Coordinate] = set()
    for y, states in enumerate(map(str.strip, lines)):
        for x, state in enumerate(states):
            if State(state) == State.Active:
                grid.add((x, y, 0))

    return grid



def load_input(input_fn: Path = Path('input')) -> Set[Coordinate]:
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def get_neighbors(coord: Coordinate):
    """
    Generates all neighbors for coordinates.
    """
    def around(axe):
        """
        """
        return ( axe-1, axe, axe+1 )

    all_neighbors = product(*( around(a) for a in coord ))

    return filter(lambda c: c != coord, all_neighbors)



def explore(grid: Set[Coordinate]):
    """
    Returns the active coordinates and their immediate neighbors.
    """
    # We want to explore the current grid and all the neighbors
    return grid | set(chain.from_iterable(get_neighbors(c) for c in grid))



def solve(active_coordinates: Set[Coordinate], num_cycles: int = 6) -> int:
    """
    Solve part 1 of the puzzle.
    """
    #print(0, sorted(active_coordinates, key=lambda c: tuple(reversed(c))))
    for turn in range(num_cycles):
        new_grid = set()
        for coord in explore(active_coordinates):
            active_neighbors = set(get_neighbors(coord)) & active_coordinates
            num_active_neighbors = len(active_neighbors)
            if coord in active_coordinates:
                # This coordinate is active.
                if 2 <= num_active_neighbors <= 3:
                    new_grid.add(coord)
            else:
                # This coordinate is inactive.
                if num_active_neighbors == 3:
                    new_grid.add(coord)
        active_coordinates = new_grid

        #print(turn+1, sorted(active_coordinates, key=lambda c: tuple(reversed(c))))
        #print(active_coordinates)

    return len(active_coordinates)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(data)

    answer = solve(data, 6)

    # 218
    print(f'Answer: {answer}')
