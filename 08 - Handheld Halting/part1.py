#!/usr/bin/env  python3

from pathlib import Path
from typing import Sequence, Tuple


def load_input(input_fn: Path = Path('input')):
    """
    Parse the puzzle's input.
    """
    with input_fn.open('r') as f:
        return tuple([ (op, int(value)) for op, value in map(str.split, (map(str.strip, f.readlines()))) ])


def execute(codes: Sequence[Tuple]) -> int:
    """
    Returns the value of the accumulator when an infinite loop is detected.
    """
    acc: int = 0
    current_instruction: int =0
    used_instructions = set()
    while True:
        if current_instruction in used_instructions:
            return acc
        op, value = codes[current_instruction]
        used_instructions.add(current_instruction)

        if op == 'nop':
            current_instruction += 1
        elif op == 'acc':
            acc += value
            current_instruction += 1
        elif op == 'jmp':
            current_instruction += value
        else:
            raise Exception(f'Invalid operation({op})')


def solve(codes: Sequence[Tuple]) -> int:
    return execute(codes)





if __name__ == '__main__':
    #codes = load_input(Path('test'))
    codes = load_input()

    if False:
        print(codes)

    answer = solve(codes)

    # 1727
    print(f'Answer: {answer}')
