from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    minval = min(A)
    maxval = max(A)
    ans = 0
    currRun = 0
    A = set(A)
    for i in range(minval, maxval+1):
        if i in A:
            currRun += 1
        else:
            ans = max(ans, currRun)
            currRun = 0
    return max(ans, currRun)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
