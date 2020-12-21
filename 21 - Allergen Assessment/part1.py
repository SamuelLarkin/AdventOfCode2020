#!/usr/bin/env  python3

from collections import (
        defaultdict,
        Counter,
        )
from dataclasses import dataclass
from itertools import (
        chain,
        groupby,
        product,
        )
from operator import itemgetter
from pathlib import Path
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



@dataclass
class Dish:
    allergens: Tuple[str]
    ingredients: Tuple[str]



def parse_input(lines: Iterable[str]):
    """
    Convert one line of the puzzle's data.
    """
    def make_dish(line: str) -> Dish:
        ingredients, _, allergens = line.partition('(contains')
        ingredients = ingredients.strip().split()
        allergens = allergens.strip()[:-1].split(',')
        allergens = tuple(map(str.strip, allergens))
        return Dish(allergens, ingredients)

    return tuple(make_dish(line.strip()) for line in lines)



def load_input(input_fn: Path = Path('input')):
    """
    Load the puzzle's data.
    """
    with input_fn.open('r') as input_f:
        return parse_input(input_f)



def find_name_allergens(dishes: Sequence[Dish]):
    """
    """
    allergen_to_ingredient = dict()
    for dish in dishes:
        for allergen in dish.allergens:
            if allergen not in allergen_to_ingredient:
                allergen_to_ingredient[allergen] = set(dish.ingredients)
            else:
                #allergen_to_ingredient[allergen] -= set(dish.ingredients)
                allergen_to_ingredient[allergen] |= set(dish.ingredients)

    return allergen_to_ingredient



def find_name_allergens2(dishes: Sequence[Dish]):
    """
    """
    ingredient_to_allergens = defaultdict(Counter)
    for dish in dishes:
        for ingredient in dish.ingredients:
            ingredient_to_allergens[ingredient].update(dish.allergens)

    return ingredient_to_allergens



def find_ingredient_count_per_allergens(dishes: Sequence[Dish]):
    """
    For each allergen, count how many times it was seen with each ingredients.
    Inspired from a translation model.
    """
    allergen_to_ingredient = defaultdict(Counter)
    for dish in dishes:
        for allergen in dish.allergens:
            allergen_to_ingredient[allergen].update(dish.ingredients)

    return allergen_to_ingredient



def find_name_allergens4(dishes: Sequence[Dish]):
    """
    """
    return Counter(chain.from_iterable(product(dish.allergens, dish.ingredients) for dish in dishes))



def find_most_likely_ingredient(counts: Counter) -> Set[str]:
    """
    Find the most likely ingredients for a given allergen.
    Returns the set of most frequent ingredient for an allergen.
    """
    # Conter keys=ingredient,  value=count
    # We need to sorted counts on the counts if we want to effectively use `groupby`
    rev = sorted((count, ingredient) for ingredient, count in counts.most_common())
    grouped = { count: set(map(itemgetter(1), group)) for count, group in groupby(rev, key=itemgetter(0)) }
    M = max(grouped.keys())

    return grouped[M]



def map_ingredient_to_allergen(dishes: Sequence[Dish]) -> Mapping[str, str]:
    """
    Find the allergen ingredient's name.
    Returns a mapping from allergen to ingredient.
    """
    # Failed
    allergen_to_ingredient = find_name_allergens(dishes)
    #print(*allergen_to_ingredient.items(), sep='\n')
    #print(*sorted(map(lambda t: (t[0], len(t[1]), t[1]), allergen_to_ingredient.items()), key=lambda t: t[1]), sep='\n')

    # Failed
    b = find_name_allergens2(dishes)
    #print(*b.items(), sep='\n', end='\n\n')

    # Failed
    d = find_name_allergens4(dishes)
    #print(*d.items(), sep='\n', end='\n\n')
    #print(*d.most_common(), sep='\n', end='\n\n')

    allergen_to_ingredient_counts = find_ingredient_count_per_allergens(dishes)
    #print('Manually extract mapping from this list', *allergen_to_ingredient_counts.items(), sep='\n', end='\n\n')
    #print('Not showing entries with same counts', *map(lambda t: (t[0], t[1].most_common(1)), allergen_to_ingredient_counts.items()), sep='\n', end='\n\n')
    most_likely_ingredient = {
            allergen: find_most_likely_ingredient(count) for allergen, count in allergen_to_ingredient_counts.items()
            }
    #print(*most_likely_ingredient.items(), sep='\n', end='\n\n')

    allergen_to_ingredient = dict()
    while len(allergen_to_ingredient) != len(most_likely_ingredient):
        # For the allergen that we haven't found a 1-to-1 mapping.
        for allergen in set(most_likely_ingredient.keys()) - set(allergen_to_ingredient.keys()):
            a = most_likely_ingredient[allergen] - set(allergen_to_ingredient.values())
            if len(a) == 1:
                allergen_to_ingredient[allergen] = a.pop()

    # Make sure there is a one-to-one mapping.
    assert len(set(allergen_to_ingredient.keys())) == len(set(allergen_to_ingredient.values()))

    if False:
        # This mapping was manually extracted from the output of `allergen_to_ingredient_counts`.
        allergen_to_ingredient = {
                'nuts': 'fvk',
                'wheat': 'zrb',
                'fish': 'kjf',
                'shellfish': 'jgtb',
                'dairy': 'rhvbn',
                'sesame': 'lbmt',
                'soy': 'hcbdb',
                'eggs': 'mmcpg',
                }

    return allergen_to_ingredient



def solve(dishes: Sequence[Dish]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    ingredient_to_allergen = map_ingredient_to_allergen(dishes)

    all_allergens = set(ingredient_to_allergen.values())
    #print(all_allergens)
    all_ingredients = chain.from_iterable(d.ingredients for d in dishes)
    non_allergen_ingredients = filter(lambda i: i not in all_allergens, all_ingredients)

    return len(list(non_allergen_ingredients))





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(*data, sep='\n')
    #print(len(data))

    answer = solve(data)

    # 2517
    assert answer == 2517
    print(f'Answer: {answer}')
