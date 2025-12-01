# 5.4

from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    m = 0
    for i,n in enumerate(A):
        if m >= len(A) or i==len(A)-1:
            return True
        if n == 0 and m <= i:
            print(n, m)
            return False
        m = max(m, i+n)

# print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
