#!/usr/bin/env  python3


from functools import reduce
from part1 import load_input
from pathlib import Path
from typing import (
        Mapping,
        Sequence,
        Tuple,
        )



def deduce_order(tickets: Tuple[Tuple[int]], constraints) -> Mapping[str, int]:
    """
    Return a mapping between a field name and its index on the ticket.
    """
    NUM_OF_FIELDS = len(tickets[0])

    # constraints per field
    field_possible_constraints = [ set(constraints.keys()) for _ in tickets[0] ]
    for ticket in tickets:
        new_possible_constraints = []
        for field, constraint in zip(ticket, field_possible_constraints):
            new_possible_constraints.append( set(filter(lambda c: field in constraints[c], constraint)))
        assert len(new_possible_constraints) == len(field_possible_constraints)
        field_possible_constraints = new_possible_constraints

    # list(len(a) for a in field_possible_constraints)
    # [2, 1, 17, 4, 18, 20, 6, 14, 12, 15, 10, 16, 7, 11, 9, 5, 8, 13, 19, 3]

    order = dict()
    seen = set()
    for cons, field_index in sorted(zip(field_possible_constraints, range(NUM_OF_FIELDS)), key=lambda a: len(a[0])):
        name = cons - seen
        assert len(name) == 1
        name = name.pop()
        order[name] = field_index
        seen |= cons

    assert len(set(order.keys())) == NUM_OF_FIELDS, 'Oups! we lost some keys.'
    assert len(set(order.values())) == NUM_OF_FIELDS, f'We should get {NUM_OF_FIELDS} distinct field indices.'

    return order



def solve(constraints, my_ticket, tickets) -> int:
    """
    Solve part 2 of the puzzle.
    """
    single_constraint = set.union(*constraints.values())
    valid_tickets = filter(lambda ticket: len(set(ticket) - single_constraint) == 0, tickets)
    valid_tickets = tuple(valid_tickets)
    fields = [ set(f) for f in zip(*valid_tickets, my_ticket) ]

    field_order = deduce_order(valid_tickets + (my_ticket,), constraints)

    departures        = filter(lambda n: n.startswith('departure'), constraints.keys())
    departure_indices = ( field_order[f] for f in departures )
    departure_values  = ( my_ticket[i] for i in departure_indices )

    return reduce(lambda a, b: a*b, departure_values, 1)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()

    answer = solve(*data)

    # 1265347500049
    print(f'Answer: {answer}')
