#!/usr/bin/env  python3


from part1 import load_input
from pathlib import Path
from tqdm import trange
from typing import Sequence


def solve(data: Sequence[int], year: int = 30_000_000) -> int:
    """
    Solve part 2 of the puzzle.
    """
    last_known_position = { k: i for i, k in enumerate(data) }

    curr = data[-1]   # Note that data[-1] occurred at len(data)-1
    # From the example
    # indices:     0 1 2
    # last spoken: 0 3 6
    for i in trange(len(data)-1, year):
        # The order of the next three instructions is crucial.
        # We delay by one recording what was last said.
        last_spoken = curr
        curr = 0 if last_spoken not in last_known_position.keys() else i - last_known_position[last_spoken]
        last_known_position[last_spoken] = i

    return last_spoken





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 1047739
    print(f'Answer: {answer}')
