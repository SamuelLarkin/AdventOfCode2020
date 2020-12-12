#!/usr/bin/env  python3


from collections import (
        namedtuple,
        )
from dataclasses import dataclass
from part1 import (
        Instruction,
        load_input,
        manhattan_distance,
        move as part1_move,
        )
from pathlib import Path
from typing import (
        Sequence,
        Tuple,
        )


Waypoint = namedtuple('Waypoint', ('x', 'y'))
#@dataclass
#class Waypoint:
#    x: int = 0
#    y: int = 0


def turn(w: Waypoint, instruction) -> Tuple[int, int]:
    """
    Turn the waypoint around the boat.
    Rotates counterclockwise
    [[ cos, -sin ]  X [[ x ], = [[ xcos - ysin ],
     [ sin,  cos ]]    [ y ]]    [ xsin + ycos ]]
    """
    if instruction in (Instruction('R', 90), Instruction('L', 270)):
        # -90
        return Waypoint(w.y, -w.x)
    elif instruction in (Instruction('R', 180), Instruction('L', 180)):
        return Waypoint(-w.x, -w.y)
    elif instruction in (Instruction('R', 270), Instruction('L', 90)):
        # +90
        return Waypoint(-w.y, w.x)
    else:
        raise Exception(f'Bad Instruction {instruction}')



def move(w: Waypoint, instruction) -> Waypoint:
    """
    Adaptor function for part1's move().
    """
    return Waypoint(*part1_move(w.x, w.y, instruction))



def solve(instructions: Sequence[int]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    waypoint = Waypoint(10, 1)
    x, y = 0, 0
    for instruction in instructions:
        if instruction.heading == 'F':
            x += instruction.distance * waypoint[0]
            y += instruction.distance * waypoint[1]
        elif instruction.heading in ('N', 'E', 'S', 'W'):
            waypoint = move(waypoint, instruction)
        elif instruction.heading in ('R', 'L'):
            waypoint = turn(waypoint, instruction)
        else:
            raise Exception('Invalid')

    return manhattan_distance(x, y)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(data)

    # 18747 
    print(f'Answer: {answer}')
