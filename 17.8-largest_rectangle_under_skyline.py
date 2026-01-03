from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(h: List[int]) -> int:
    s,s2 = [], []
    l = len(h)
    minLeft = {}
    minRight = {}
    for i in range(l):
        curr = h[i]
        while s and h[s[-1]] >= curr:
            s.pop()
        if s:
            minLeft[i] = s[-1]
        else:
            minLeft[i] = -1
        s.append(i)
        j = l-i-1
        curr = h[j]
        while s2 and h[s2[-1]] >= curr:
            s2.pop()
        if s2:
            minRight[j] = s2[-1]
        else:
            minRight[j] = l
        s2.append(j)
    m = 0
    for i in range(l):
        m = max(m, h[i]*(minRight[i]-minLeft[i]-1))
    return m


# print(calculate_largest_rectangle([1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
