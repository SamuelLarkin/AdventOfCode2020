#!/usr/bin/env  python3

from collections import (
        namedtuple,
        )
from pathlib import Path
from typing import (
        Iterable,
        Sequence,
        Tuple,
        )


Instruction = namedtuple('Instruction', ('heading', 'distance'))


TURNS = {
        ('N', 'R90'): 'E',
        ('N', 'R180'): 'S',
        ('N', 'R270'): 'W',
        ('E', 'R90'): 'S',
        ('E', 'R180'): 'W',
        ('E', 'R270'): 'N',
        }


def parse_input(lines: str) -> int:
    """
    Convert one line of the puzzle's data.
    """
    return tuple(Instruction(line[0], int(line[1:])) for line in lines)



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def manhattan_distance(x: int, y: int) -> int:
    """
    """
    if x < 0:
        x = -x
    if y < 0:
        y = -y

    return x + y



def move(x: int, y: int, instruction) -> Tuple[int, int]:
    """
    """
    if instruction.heading == 'N':
        y += instruction.distance
    elif instruction.heading == 'S':
        y -= instruction.distance
    elif instruction.heading == 'E':
        x += instruction.distance
    elif instruction.heading == 'W':
        x -= instruction.distance
    else:
        raise Exception('Unsupported')

    return x, y


def turn(heading, instruction):
    """
    Turn the boat.
    """
    rotations = ('N', 'E', 'S', 'W')
    mapping = { d: i for i, d in enumerate(rotations) }
    offset = int(instruction.distance / 90)
    if instruction.heading == 'L':
        offset *= -1

    return rotations[(mapping[heading] + offset)%4]



def solve(instructions: Sequence[int]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    direction = 'E'
    x, y = 0, 0
    for instruction in instructions:
        if instruction.heading in ('R', 'L'):
            direction = turn(direction, instruction)
        elif instruction.heading == 'F':
            x, y = move(x, y, Instruction(direction, instruction.distance))
        else:
            x, y = move(x, y, instruction)

    return manhattan_distance(x, y)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    print(data)

    answer = solve(data)

    # 904
    print(f'Answer: {answer}')
