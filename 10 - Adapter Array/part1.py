#!/usr/bin/env  python3

from collections import Counter
from pathlib import Path
from typing import Sequence


def load_input(input_fn: Path = Path('input')):
    with input_fn.open('r') as input_f:
        return tuple(map(int, input_f))


def solve(data: Sequence[int]) -> int:
    data += tuple([0, max(data)+3])
    data = sorted(data)
    jolts = Counter(b - a for a, b in zip(data, data[1:]))

    return jolts[1] * jolts[3]





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 2310
    print(f'Answer: {answer}')
