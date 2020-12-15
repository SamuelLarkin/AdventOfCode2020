#!/usr/bin/env  python3

from collections import (
        defaultdict,
        )
from pathlib import Path
from typing import (
        Iterable,
        Sequence,
        )


def parse_input(line: Iterable) -> int:
    """
    Convert one line of the puzzle's data.
    """
    return tuple(int(v) for v in line.strip().split(','))


def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f.readline())


def solve(data: Sequence[int], maximum_turn: int = 2020) -> int:
    """
    Solve part 1 of the puzzle.
    """
    last_known_position = defaultdict(lambda: [])
    last_known_position.update({k: [i] for i, k in enumerate(data)})
    last_spoken = data[-1]
    for t in range(len(data), 2020):
        if last_spoken in last_known_position:
            if len(last_known_position[last_spoken]) == 1:
                last_spoken = 0
            else:
                values = last_known_position[last_spoken]
                assert len(values) > 1
                last_spoken = values[-1] - values[-2]
        last_known_position[last_spoken].append(t)

    return last_spoken





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #data = (0, 3, 6)

    answer = solve(data)

    # 517
    print(f'Answer: {answer}')
