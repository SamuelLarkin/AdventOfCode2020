#!/usr/bin/env  python3

from collections import Counter
from functools import reduce
from part1 import survey_gen
from typing import Sequence


def common_answers(surveys: Sequence[frozenset]) -> frozenset:
    """
    Given a group's survey answers, find the common questions.
    """
    return frozenset.intersection(*surveys)





if __name__ == '__main__':
    same_answers = map(common_answers, survey_gen())
    answer = sum(map(len, same_answers))

    # 3406
    print(f'Answer: {answer}')
