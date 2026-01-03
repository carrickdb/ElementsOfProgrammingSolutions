import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals: List[Interval]) -> int:
    intervals.sort(key=lambda x: x[1])
    num_visits = 0
    prev = None
    for s,e in intervals:
        if prev==None:
            prev = e
            num_visits += 1
            continue
        if prev < s:
            num_visits += 1
            prev = e
        elif e < prev:
            num_visits += 1

    return num_visits




@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
