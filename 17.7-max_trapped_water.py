from typing import List

from test_framework import generic_test


def get_max_trapped_water(h: List[int]) -> int:
    p1,p2 = 0, len(h)-1
    m = 0
    while p1 < p2:
        m = max(m, min(h[p1],h[p2])*(p2-p1))
        if h[p1] < h[p2]:
            p1 += 1
        else:
            p2 -= 1
    return m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
