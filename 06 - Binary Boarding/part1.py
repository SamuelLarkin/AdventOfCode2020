#!/usr/bin/env  python3

from collections import Counter
from typing import Sequence


def survey_gen():
    """
    Reads one group's survey at a time.
    """
    with open('input', 'r') as f:
        surveys = []
        for l in map(str.strip, f):
            if l == '':
                yield surveys
                surveys = []
            else:
                surveys.append(frozenset(l))

    yield surveys


def all_answers(surveys: Sequence[frozenset]) -> frozenset:
    """
    What are all the questions that were answered yes in a group.
    """
    return frozenset.union(*surveys)






if __name__ == '__main__':
    yes_answers = map(all_answers, survey_gen())
    answer = sum(map(len, yes_answers))

    # 6778
    print(f'Answer: {answer}')
