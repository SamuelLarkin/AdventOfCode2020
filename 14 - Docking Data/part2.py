#!/usr/bin/env  python3


from part1 import load_input
from pathlib import Path
from typing import (
        Iterable,
        Tuple,
        )


INSTRUCTION_LEN = 36


def addresses(address: str, mask: str, prefix: str = '') -> int:
    """
    A generator of all possible addresses when substituting X by {0, 1}.
    """
    assert len(address) == len(mask)
    assert len(address) + len(prefix) == INSTRUCTION_LEN

    if len(address) == 0:
        assert len(prefix) == INSTRUCTION_LEN
        yield prefix
    else:
        for i, (a, m) in enumerate(zip(address, mask), 1):
            if m == '0':
                prefix += a
            elif m == '1':
                prefix += '1'
            elif m == 'X':
                yield from addresses(address[i:], mask[i:], prefix + '0')
                yield from addresses(address[i:], mask[i:], prefix + '1')
                break
        else:
            # Case where it doesn't end with 'X'
            yield prefix



def parse_mem(instruction: str) -> Tuple[str, int]:
    """
    """
    address, _, value = instruction.split()
    value = int(value)
    address = address[4:][:-1]
    address = bin(int(address))[2:]
    address = address.zfill(INSTRUCTION_LEN)

    return address, value



def solve(data: Iterable[str]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    mem = dict()
    mask = None
    for instruction in map(str.strip, data):
        if instruction.startswith('mask'):
            mask = instruction.split('=')[1].strip()
        elif instruction.startswith('mem'):
            address, value = parse_mem(instruction)
            assert len(address) == INSTRUCTION_LEN
            assert len(address) == len(mask)
            for a in addresses(address, mask):
                a = int(a, 2)
                mem[a] = value
        else:
            raise Exception(f'Invalid instruction {instruction}')

    return sum(mem.values(), 0)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 3289441921203
    print(f'Answer: {answer}')
