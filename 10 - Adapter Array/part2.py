#!/usr/bin/env  python3


from functools import lru_cache
from part1 import load_input
from pathlib import Path
from typing import Sequence


@lru_cache(maxsize=None)
def recurse(data: Sequence[int], start: int, end: int) -> int:
    if start == end:
        return 1

    return sum((recurse(data, s, end) for s in range(start+1, start+3+1) if s in data), 0)


def solve(data: Sequence[int]) -> int:
    s = 0
    e = max(data)

    return recurse(data, s, e)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 64793042714624
    print(f'Answer: {answer}')
