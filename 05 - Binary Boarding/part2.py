#!/usr/bin/env  python3

from part1 import load_input





if __name__ == '__main__':
    for sit in load_input():
        print(sit)

    sits = list(load_input())
    sit_min = min(sits, key=lambda s: s.id)
    sit_max = max(sits, key=lambda s: s.id)
    print(sit_min, sit_max)

    answer = set(range(sit_min.id, sit_max.id)) - set(s.id for s in sits)

    # 705
    print(f'Answer: {answer}')
