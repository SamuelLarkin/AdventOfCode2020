#!/usr/bin/env  python3


def load_input():
    with open('input', mode='r') as f:
        expenses = set(map(int ,map(str.strip, f.readlines())))

    return expenses



def solve(expenses):
    for v in expenses:
        w = 2020 - v
        if w in expenses:
            return v, w






if __name__ == '__main__':
    expenses = load_input()
    v, w = solve(expenses)
    assert v + w == 2020

    # 713184
    print(v, w)
    print(f'Answer: {v*w}')
