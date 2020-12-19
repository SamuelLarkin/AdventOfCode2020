#!/usr/bin/env  python3

import re

from collections import (
        defaultdict,
        )
from itertools import (
        chain,
        )
from pathlib import Path
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



def parse_input(lines: Iterable[str]):
    """
    Convert one line of the puzzle's data.
    """
    number_re = re.compile(r'\d+')
    space_re  = re.compile(r'\s+')
    rules = dict()
    converted_rule_indices = set()
    for line in map(str.strip, lines):
        if line == '':
            break
        index, rule = map(str.strip, line.split(':'))
        if '"' in rule:
            converted_rule_indices.add(index)
            rule = rule[1:-1]
        rules[index] = rule

    while len(converted_rule_indices) < len(rules):
        for index in set(rules) - converted_rule_indices:
            rs = set(filter(lambda a: a!= '|', rules[index].split()))
            if len(rs - converted_rule_indices) == 0:
                rule = number_re.sub(lambda m: rules[m.group()], rules[index])
                rule = space_re.sub('', rule)
                rules[index] = f'({rule})'
                converted_rule_indices.add(index)

    return rules, tuple(map(str.strip, lines))



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def solve(rules: Mapping, data: Sequence[str]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    rule_to_match = re.compile(f"^{rules['0']}$")
    matched = filter(lambda d: rule_to_match.match(d) != None, data)

    return len(list(matched))





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    rules, data = load_input()
    #print(rules, data)

    answer = solve(rules, data)

    # 220
    print(f'Answer: {answer}')
