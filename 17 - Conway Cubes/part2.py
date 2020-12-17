#!/usr/bin/env  python3


from part1 import (
        Coordinate,
        Coordinate3D,
        Coordinate4D,
        load_input,
        solve as solve1,
        )
from pathlib import Path
from typing import (
        Sequence,
        Set,
        Tuple,
        )


def convert_coordinate_to_4d(coordinates : Set[Coordinate3D]) -> Set[Coordinate4D]:
    """
    Converts 3d coordinates to 4d coordinates.
    """
    return set(( c + (0,) for c in coordinates ))



def solve(active_coordinates: Set[Coordinate], num_cycles: int = 6) -> int:
    """
    Solve part 2 of the puzzle.
    """
    active_coordinates = convert_coordinate_to_4d(active_coordinates)

    return solve1(active_coordinates, num_cycles)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 1908 
    print(f'Answer: {answer}')
