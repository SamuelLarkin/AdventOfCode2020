#!/usr/bin/env  python3

from itertools import (
        chain,
        )
from pathlib import Path
from typing import (
        Iterable,
        Sequence,
        )


def parse_input(lines: Iterable):
    """
    Convert one line of the puzzle's data.
    """
    constraints = dict()
    for line in map(str.strip, lines):
        if line == '':
            break
        field, values = line.split(':')
        c1, c2 = tuple(tuple(map(int, c.split('-'))) for c in values.split('or'))
        constraints[field] = set(range(c1[0], c1[1]+1)) | set(range(c2[0], c2[1]+1))

    assert lines.readline().strip() == 'your ticket:'
    my_ticket = tuple(map(int, lines.readline().strip().split(',')))

    assert lines.readline().strip() == ''
    assert lines.readline().strip() == 'nearby tickets:'
    tickets = tuple(tuple(map(int, l.split(','))) for l in map(str.strip, lines))

    return constraints, my_ticket, tickets



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)


def solve(constraints, my_ticket, tickets) -> int:
    """
    Solve part 1 of the puzzle.
    """
    single_constraint = set.union(*constraints.values())
    invalid_fields = map(lambda ticket: set(ticket) - single_constraint, tickets)
    #print(*invalid_fields, sep='\n')

    return sum(chain.from_iterable(invalid_fields), 0)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(data)

    answer = solve(*data)

    # 25984
    print(f'Answer: {answer}')
