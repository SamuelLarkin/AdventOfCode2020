from sllist import (
        Node,
        make_circular_list,
        )
from tqdm import trange
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )



def play_a_round(
        current_cup: Node,
        NUM_CARDS: int,
        move: int,
        ) -> Node:
    """
    """
    #print(f'-- move {move+1} --')
    #print('cups:', '  '.join(map(str, data)))
    # The crab picks up the three cups that are immediately clockwise of
    # the current cup. They are removed from the circle; cup spacing is
    # adjusted as necessary to maintain the circle.
    trio = current_cup.remove_trio()
    #print('pick up:', ', '.join(map(str, three_cups)))

    # The crab selects a destination cup: the cup with a label equal to the
    # current cup's label minus one. If this would select one of the cups
    # that was just picked up, the crab will keep subtracting one until it
    # finds a cup that wasn't just picked up. If at any point in this
    # process the value goes below the lowest value on any cup's label, it
    # wraps around to the highest value on any cup's label instead.
    destination_cup_value = current_cup.data - 1
    exclusion = set((trio.data, trio.next.data, trio.next.next.data))
    while destination_cup_value in exclusion or destination_cup_value < 1:
        destination_cup_value -= 1
        if destination_cup_value < 1:
            destination_cup_value = NUM_CARDS
    #print('destination:', destination_cup_value)

    # The crab places the cups it just picked up so that they are
    # immediately clockwise of the destination cup. They keep the same
    # order as when they were picked up.
    destination_cup = current_cup.find(destination_cup_value)
    destination_cup.reinsert_trio(trio)

    # The crab selects a new current cup: the cup which is immediately
    # clockwise of the current cup.
    # NOTE: data has changed and so will the current index thus we find it again.
    current_cup = current_cup.next

    #print()

    return current_cup



def play_game(data: Tuple[int], num_rounds: int = 100):
    current_cup = make_circular_list(data)
    for move in range(num_rounds):
        current_cup = play_a_round(current_cup, len(data), move)

    return current_cup
