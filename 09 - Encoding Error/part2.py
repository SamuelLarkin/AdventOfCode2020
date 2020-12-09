#!/usr/bin/env  python3

from part1 import load_input
from typing import Sequence


def solve(data: Sequence[int], target: int) -> int:
    """
    Return the min + max, the minimum number and the maximum number found in
    the range of values that sum to part1's answer.
    """
    for s in range(len(data)):
        for e in range(s+1, len(data)):
            possible_values = data[s:e]
            somme = sum(data[s:e])
            if somme == target:
                return min(possible_values) + max(possible_values)
            elif somme > target:
                break




if __name__ == '__main__':
    data   = load_input()
    answer = solve(data, 217430975)

    # 28509180
    print(f'Answer: {answer}')
