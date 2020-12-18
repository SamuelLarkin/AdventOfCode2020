#!/usr/bin/env  python3

from collections import (
        defaultdict,
        )
from itertools import (
        chain,
        )
from pathlib import Path
from typing import (
        Iterable,
        Iterator,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



def parse_input(lines: Iterable[str]):
    """
    Convert one line of the puzzle's data.
    """
    no_newline = map(str.strip, lines)

    return tuple(list(''.join(l.split())) for l in no_newline)



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def operate(lvalue: int, rvalue: int, op: str) -> int:
    """
    Applies the operation.
    """
    if op == '+':
        return rvalue + lvalue
    elif op == '*':
        return rvalue * lvalue
    else:
        raise Exception('No op')



def calculate(data: Tuple, total: int = 0) -> int:
    """
    Evaluate the expression from left-to-right where '+' & '*' have the same precedence.
    """
    last_op = '+'
    total = 0
    value = None
    while len(data) > 0:
        c = data.pop(0)
        if c == '(':
            value = calculate(data)
            total = operate(total, value, last_op)
        elif c == ')':
            return total
        elif c in ('+', '*'):
            last_op = c
        else:
            value = int(c)
            total = operate(total, value, last_op)

    return total



def solve(data: Sequence[str]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    return sum(calculate(l) for l in data)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(*data, sep='\n')

    answer = solve(data)

    # 5783053349377
    print(f'Answer: {answer}')
