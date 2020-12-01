#!/usr/bin/env  python3

from part1 import load_input



def solve(expenses):
    for a in expenses:
        for b in expenses:
            c = 2020 - a - b
            if c in expenses:
                return a, b, c





if __name__ == '__main__':
    expenses = load_input()
    a, b, c = solve(expenses)
    assert a + b + c == 2020

    # 261244452
    print(a, b, c)
    print(f'Answer: {a * b * c}')
