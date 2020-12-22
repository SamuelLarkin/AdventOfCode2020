#!/usr/bin/env  python3


from enum import Enum
from part1 import (
        load_input,
        )
from pathlib import Path
from typing import (
        Iterable,
        Mapping,
        Sequence,
        Set,
        Tuple,
        )


class PlayerID(Enum):
    player1 = 0
    player2 = 1



def play_game(
        deck1: Sequence[int],
        deck2: Sequence[int],
        ) -> Sequence[int]:
    """
    Plays the recursive game.
    Returns the winner's deck.
    """
    previous_configurations = set()
    while len(deck1) > 0 and len(deck2) > 0:
        #print("Player 1's deck:", ', '.join(map(str, deck1)))
        #print("Player 2's deck:", ', '.join(map(str, deck2)))

        # Before either player deals a card, if there was a previous round in
        # this game that had exactly the same cards in the same order in the
        # same players' decks, the game instantly ends in a win for player 1.
        # Previous rounds from other games are not considered. (This prevents
        # infinite games of Recursive Combat, which everyone agrees is a bad
        # idea.)
        configuration = (tuple(deck1), tuple(deck2))
        if configuration in previous_configurations:
            return PlayerID.player1, deck1

        previous_configurations.add(configuration)

        # Otherwise, this round's cards must be in a new configuration; the
        # players begin the round by each drawing the top card of their deck as
        # normal.
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        #print("Player 1 plays:", card1)
        #print("Player 2 plays:", card2)

        # If both players have at least as many cards remaining in their deck
        # as the value of the card they just drew, the winner of the round is
        # determined by playing a new game of Recursive Combat (see below).
        if len(deck1) >= card1 and len(deck2) >= card2:
            sub_deck1 = deck1[:card1]
            sub_deck2 = deck2[:card2]
            winner_id, winner_deck = play_game(sub_deck1, sub_deck2)
            if winner_id == PlayerID.player1:
                #print('Player 1 wins')
                deck1.extend((card1, card2))
            elif winner_id == PlayerID.player2:
                #print('Player 2 wins')
                deck2.extend((card2, card1))
            else:
                raise Exception(f'Could not find the proper deck')
        # Otherwise, at least one player must not have enough cards left in
        # their deck to recurse; the winner of the round is the player with the
        # higher-value card.
        else:
            if card1 > card2:
                #print('Player 1 wins')
                deck1.extend((card1, card2))
            elif card2 > card1:
                #print('Player 2 wins')
                deck2.extend((card2, card1))
            else:
                assert card1 != card2

    if len(deck1) > 0:
        return PlayerID.player1, deck1
    else:
        return PlayerID.player2, deck2



def solve(deck1: Sequence[int], deck2: Sequence[int]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    winner_id, winner_deck = play_game(deck1, deck2)

    # After the game, the winning player's score is calculated from the cards
    # they have in their original deck using the same rules as regular Combat.
    return sum((a*(b+1) for a, b in zip(reversed(winner_deck), range(len(winner_deck)))))





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    deck1, deck2 = load_input()

    answer = solve(deck1, deck2)

    # 35836
    print(f'Answer: {answer}')
    assert answer == 35836
