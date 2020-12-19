#!/usr/bin/env  python3

from typing import (
        Sequence,
        )


def shunting_yard_for_part1(data: str) -> Sequence:
    """
    [Shunting Yard Algorithm](https://brilliant.org/wiki/shunting-yard-algorithm/)
    7 * (7 * 6 + 7 * 5 + (9 + 2 * 2 * 4)) + 7 * 3 * 5
    7 7 6 * 7 + 5 * 9 2 + 2 * 4 * + * 7 + 3 * 5 *
    """
    queue = []
    stack = []
    for c in data:
        if c in '*+':
            if len(stack) > 0:
                d = stack.pop(-1)
                if d != '(':
                    queue.append(d)
            stack.append(c)
        elif c == '(':
            stack.append(c)
            pass
        elif c == ')':
            queue.append(stack.pop(-1))
            #while stack[-1] != '(':
            #    queue.append(stack.pop(-1))
            #assert stack.pop(-1) == '('
        else:
            queue.append(int(c))

    queue.extend(reversed(stack))

    return queue



def shunting_yard(data: str, most_precedent_operator: str = '*') -> Sequence:
    """
    [Shunting Yard Algorithm](https://brilliant.org/wiki/shunting-yard-algorithm/)
    """
    queue = []
    stack = []
    for c in data:
        if c in '*+':
            while len(stack) > 0 and stack[-1] == most_precedent_operator:
                queue.append(stack.pop(-1))
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                queue.append(stack.pop(-1))
            assert stack.pop(-1) == '('
        else:
            queue.append(int(c))

    queue.extend(reversed(stack))

    return queue



def evaluate_reversed_polish_notation(expression) -> int:
    """
    """
    stack = []
    for c in expression:
        if isinstance(c, int):
            stack.append(c)
        else:
            rvalue = stack.pop(-1)
            lvalue = stack.pop(-1)
            if c == '*':
                stack.append(rvalue * lvalue)
            else:
                stack.append(rvalue + lvalue)

    assert len(stack) == 1

    return stack.pop()





if __name__ == '__main__':
    rpn = shunting_yard('2 * 3 + ( 4 * 5 )'.split())
    print(rpn)
    print(evaluate_reversed_polish_notation(rpn))

    rpn = shunting_yard('2 * 3 + ( 4 * 5 )'.split(), '+')
    print(rpn)
    print(evaluate_reversed_polish_notation(rpn))
