#!/usr/bin/env  python3

from pathlib import Path
from typing import Sequence


def parse_input(line: str) -> int:
    """
    Convert one line of the puzzle's data.
    """
    return int(line.strip())


def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return list(map(parse_input, input_f))


def solve(data: Sequence[int]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    return 1





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    print(f'Answer: {answer}')
