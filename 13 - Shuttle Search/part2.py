#!/usr/bin/env  python3


from functools import reduce
from part1 import (
        Schedule,
        )
from pathlib import Path
from typing import (
        Sequence,
        Tuple,
        Iterable,
        )



def chinese_remainder(n: Sequence[int], a: Sequence[int]) -> int:
    """
    [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
    [Python Implementation of Chinese Remainder Theorem](https://rosettacode.org/wiki/Chinese_remainder_theorem#Python)
    """
    total = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * multiplicative_inverse(p, n_i) * p

    return total % prod
 
 
 
def multiplicative_inverse(a: int, b: int) -> int:
    """
    [Modular Multiplicative Inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)
    """
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1
 
 

def parse_input(lines: Iterable) -> int:
    """
    Convert one line of the puzzle's data.
    """
    lines = list(lines)
    assert len(lines) == 2
    time = int(lines[0])
    positional = enumerate(lines[1].split(','))
    nox = filter(lambda x: x[1]!='x', positional)
    buses = tuple(map(lambda d: (d[0], int(d[1])), nox))
    return Schedule(time, buses)



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def solve(schedule: Schedule) -> int:
    """
    Solve part 2 of the puzzle.
    """
    bus = sorted(schedule.bus, key=lambda d: d[1])
    bus = tuple((b-a, b) for a, b in bus)
    a, n = zip(*bus)

    return chinese_remainder(n, a)





if __name__ == '__main__':
    #data = load_input(Path('test'))
    #data = load_input(Path('test2'))
    data = load_input()
    print(data)

    answer = solve(data)

    # 225850756401039 
    print(f'Answer: {answer}')
