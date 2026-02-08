from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # array:  2 4 3 7 4 6 8 2 5
    # actual: 5 2 8 6 4 7 3 4 2
    s = []
    for i, building in enumerate(sequence):
        while s and s[-1][1] <= building:
            s.pop()
        s.append((i, building))
    return [i for i,_ in s][::-1]

    # s = []
    # i = 0
    # for building in sequence:
    #     s.append((building, i))
    #     i += 1
    # ans = []
    # m = 0
    # while s:
    #     curr, i = s.pop()
    #     if curr > m:
    #         m = curr
    #         ans.append(i)
    # return ans

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
