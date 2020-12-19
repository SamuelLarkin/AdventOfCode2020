#!/usr/bin/env  python3


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



def evaluate(expression: str) -> int:
    """
    Once we have no parenthesis
    """
    if '*' in expression:
        left, _, right = expression.partition('*')
        return evaluate(left) * evaluate(right)
    elif '+' in expression:
        left, _, right = expression.partition('+')
        return evaluate(left) + evaluate(right)
    else:
        return int(expression)



def lexer(expression: str):
    """
    Not really a lexer because it actually builds a tree.
    """
    retour = []
    while len(expression) > 0:
        c = expression.pop(0)
        if c == '(':
            count = 1
            sube = []
            while count > 0:
                d = expression.pop(0)
                if d == '(':
                    count += 1
                elif d == ')':
                    count -= 1
                sube += d
            retour.append(lexer(sube[:-1]))
        elif c in ('*', '+'):
            retour.append(c)
        else:
            #retour.append(int(c))
            retour.append(c)

    return retour



def parse(lexed) -> int:
    """
    """
    if isinstance(lexed, int):
        return lexed

    for i in range(len(lexed)):
        a = lexed[i]
        if isinstance(a, list):
            lexed[i] = parse(a)

    return evaluate(''.join(map(str, lexed)))



def solve(expressions: Sequence[int]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    lexed = map(lexer, expressions)
    solved = map(parse, lexed)

    return sum(solved)





if __name__ == '__main__':
    #data = load_input(Path('test1'))
    #data = load_input(Path('test2'))
    data = load_input()
    #print(data)

    answer = solve(data)

    # 74821486966872
    print(f'Answer: {answer}')
