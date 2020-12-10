#!/usr/bin/env  python3


from part1 import load_input
from pathlib import Path
from typing import Sequence


def solve(data: Sequence[int]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    return 1





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 
    print(f'Answer: {answer}')
