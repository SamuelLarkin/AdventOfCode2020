#!/usr/bin/env  python3

from collections import defaultdict
from pathlib import Path


MY_BAG = 'shiny gold'


def name(name: str) -> str:
    """
    Drop bag/bags from the name.
    """
    return ' '.join(name.strip().split()[:-1])


def drop_count(name: str) -> str:
    """
    Remove the count from the name.
    """
    name = name.strip()
    count, *names = name.split()
    return ' '.join(names)


def load_input(input_fn: Path = Path('input')):
    """
    wavy turquoise bags contain no other bags.
    vibrant beige bags contain 4 drab lime bags, 1 muted violet bag, 5 drab plum bags, 5 shiny silver bags.
    """
    holder = defaultdict(set)
    with input_fn.open('r') as f:
        for l in map(str.strip, f):
            l = l.strip('.')
            carrier_bag, content = l.split('contain')
            carrier_bag = name(carrier_bag)
            bags = tuple(map(drop_count, map(name, content.split(','))))
            for bag in bags:
                holder[bag].add(carrier_bag)


    return holder



def solver(bag: str, holders) -> int:
    possible_colors = holders[bag]
    last_size = len(possible_colors)
    while True:
        possible_colors = possible_colors.union(*[ holders[s] for s in possible_colors ])
        if last_size == len(possible_colors):
            break
        last_size = len(possible_colors)

    return len(possible_colors)





if __name__ == '__main__':
    #holders = load_input(Path('test'))
    holders = load_input()
    #print(holders)
    #print(holders[MY_BAG])

    answer = solver(MY_BAG, holders)

    # 222
    print(f'Answer: {answer}')
