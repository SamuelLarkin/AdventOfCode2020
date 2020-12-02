#!/usr/bin/env  python3

from collections import Counter


def parse(line):
    r, l, p = line.split()
    l = l[0]
    m, M = r.split('-')

    return int(m), int(M), l, p






if __name__ == '__main__':
    num_valid = 0
    with open('input', 'r') as f:
        for entry in map(str.strip, f):
            m, M, l, p = parse(entry)
            c = Counter(p)
            if l in c and (m <= c[l] <= M):
                num_valid += 1


    # 542
    print(f'Answer: {num_valid}')
