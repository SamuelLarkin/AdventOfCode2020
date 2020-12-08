#!/usr/bin/env  python3

from part1 import load_input
from pathlib import Path
from typing import Sequence, Tuple


def nop_jmp(codes: Sequence[Tuple]):
    """
    Generator of alter code instructions.
    """
    for i, (op, value) in enumerate(codes):
        if op == 'jmp':
            altered_code = list(codes)
            altered_code[i] = ('nop', value)
            yield altered_code
        elif op == 'nop':
            altered_code = list(codes)
            altered_code[i] = ('nop', value)
            yield altered_code


class InfiniteLoop(Exception):
    """
    Exception signaling a set of code instructions that will never finish aka
    will perform infinite loop.
    """
    pass


def execute(codes: Sequence[Tuple]) -> int:
    """
    Runs a set of instructions.
    Either throws and exception if an infinite loop is detected or returns the
    value of the accumulator.
    """
    acc: int = 0
    current_instruction: int =0
    used_instructions = set()
    while True:
        if current_instruction in used_instructions:
            raise InfiniteLoop()
        if current_instruction >= len(codes):
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


def solve(codes: Sequence[Tuple]):
    """
    Alters the program's instruction one instruction at a time and verifies that it runs fine.
    """
    for altered_code in nop_jmp(codes):
        try:
            return execute(altered_code)
        except InfiniteLoop:
            pass





if __name__ == '__main__':
    #codes = load_input(Path('test'))
    codes = load_input()

    if False:
        nop_ops = filter(lambda c: c[0] == 'nop', codes)
        print(len(list(nop_ops)))

        jmp_ops = filter(lambda c: c[0] == 'jmp', codes)
        print(len(list(jmp_ops)))

    answer = solve(codes)

    # 552
    print(f'Answer: {answer}')
