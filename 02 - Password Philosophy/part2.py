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
            # Convert indices to 0-based index.
            m -= 1
            M -= 1
            assert m < len(p)
            assert M < len(p)
            if (p[m] == l and p[M] != l) or (p[m] != l and p[M] == l):
                num_valid += 1


    # 360
    print(f'Answer: {num_valid}')
