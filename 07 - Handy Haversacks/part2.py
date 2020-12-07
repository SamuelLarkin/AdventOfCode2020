#!/usr/bin/env  python3


from collections import Counter
from collections import defaultdict
from part1 import name
from part1 import drop_count
from pathlib import Path


MY_BAG = 'shiny gold'


def subbags(content: str) -> dict:
    bags = list(map(str.strip, content.strip().split(',')))

    retour = dict()
    for bag in map(str.strip, bags):
        if bag != 'no other bags':
            count, *names = bag.split()
            names = name(' '.join(names))
            retour[names] = int(count)

    return retour


def load_input(input_fn: Path = Path('input')):
    """
    wavy turquoise bags contain no other bags.
    vibrant beige bags contain 4 drab lime bags, 1 muted violet bag, 5 drab plum bags, 5 shiny silver bags.
    """
    holder = defaultdict(dict)
    with input_fn.open('r') as f:
        for l in map(str.strip, f):
            l = l.strip('.')
            carrier_bag, content = l.split('contain')
            carrier_bag = name(carrier_bag)
            holder[carrier_bag] = subbags(content)

    return holder


def solver(bag_name: str, rules) -> int:
    """
    Recursively count the number of bags in a bag.
    """
    return sum( count * (1 + solver(name, rules)) for name, count in rules[bag_name].items() )






if __name__ == '__main__':
    #rules = load_input(Path('test'))
    #rules = load_input(Path('test2'))
    rules = load_input()
    #print(rules)
    #print(rules[MY_BAG])
    answer = solver(MY_BAG, rules)

    # 13264
    print(f'Answer: {answer}')
