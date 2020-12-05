#!/usr/bin/env  python3

import math
import re


class Sit:
    __slots__ = ('row', 'column')

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    @property
    def id(self):
        return 8 * self.row + self.column

    def __str__(self):
        return f'id: {self.id} row: {self.row} column: {self.column}'


def parse_row(row: str) -> int:
    number = 0
    for i, c in enumerate(row[::-1]):
        if c == 'B':
            number += int(math.pow(2, i))

    return number


def parse_column(column: str) -> int:
    number = 0
    for i, c in enumerate(column[::-1]):
        if c == 'R':
            number += int(math.pow(2, i))

    return number


def parse_sit(data: str):
    row = parse_row(data[:7])
    column = parse_column(data[7:])
    return Sit(row, column)


def load_input():
    with open('input', 'r') as f:
        for l in map(str.strip, f):
            yield parse_sit(l)





if __name__ == '__main__':
    for sit in load_input():
        print(sit)
    print(parse_sit('FBFBBFFRLR'))

    answer = max(load_input(), key=lambda s: s.id)

    # 822
    print(f'Answer: {answer.id}')
