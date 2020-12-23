from tqdm import trange
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



def play_a_round(
        next_cups: Sequence[int],
        current_cup: int,
        ) -> int:
    """
    array where arr[cup] = next_cup
    """
    NUM_CARDS = len(next_cups) - 1

    # The crab picks up the three cups that are immediately clockwise of
    # the current cup. They are removed from the circle; cup spacing is
    # adjusted as necessary to maintain the circle.
    trio1 = next_cups[current_cup]
    trio2 = next_cups[trio1]
    trio3 = next_cups[trio2]
    next_cups[current_cup] = next_cups[trio3]

    # The crab selects a destination cup: the cup with a label equal to the
    # current cup's label minus one. If this would select one of the cups
    # that was just picked up, the crab will keep subtracting one until it
    # finds a cup that wasn't just picked up. If at any point in this
    # process the value goes below the lowest value on any cup's label, it
    # wraps around to the highest value on any cup's label instead.
    destination_cup = current_cup - 1
    exclusion = set((trio1, trio2, trio3))
    while destination_cup in exclusion or destination_cup < 1:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = NUM_CARDS
    #print('destination:', destination_cup)

    # The crab places the cups it just picked up so that they are
    # immediately clockwise of the destination cup. They keep the same
    # order as when they were picked up.
    next_cups[trio3] = next_cups[destination_cup]
    next_cups[destination_cup] = trio1

    # The crab selects a new current cup: the cup which is immediately
    # clockwise of the current cup.
    # NOTE: data has changed and so will the current index thus we find it again.
    current_cup = next_cups[current_cup]

    return current_cup



def play_game(data: Tuple[int], num_rounds: int = 100):
    """
    Play the game using an array where arr[cup] = next_cup
    """
    current_cup = data[0]
    next_cups = [None] * (len(data) + 1)
    for c, n in zip(data, data[1:]):
        next_cups[c] = n
    next_cups[data[-1]] = data[0]
    assert len(set(next_cups)) == len(next_cups)

    for move in trange(num_rounds):
        current_cup = play_a_round(next_cups, current_cup)

    return next_cups
