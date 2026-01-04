from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(h: List[int]) -> int:
    s = []
    m = 0
    for i,b in enumerate(h+[0]):
        while s and h[s[-1]] >= b:
            prevBuilding = s.pop()
            height = h[prevBuilding]
            width = i if not s else i-s[-1]-1
            m = max(m, height*width)
        s.append(i)
    return m

    # This doesn't work (calculating from the last building in a series as opposed to the building after it)
    # because it doesn't account for the rectangles going forwards from a shorter building to longer.
    # s = [0]
    # h = [-1] + h
    # m = 0
    # l = len(h)
    # for i in range(1, l):
    #     b = h[i]
    #     while s and h[s[-1]] >= b:
    #         s.pop()
    #     width = (i - s[-1])
    #     print(i, b, width, width*b)
    #     m = max(m, width * b)
    #     s.append(i)
    # return m

# print(calculate_largest_rectangle([3,2,1]))
# print(calculate_largest_rectangle([1,2,3]))


# test 1

#0  1  2  3  4  5  6  7  8  9 10 11 12
# [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
