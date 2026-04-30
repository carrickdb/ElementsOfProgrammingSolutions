from typing import Iterator, List

from test_framework import generic_test

import heapq

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    h = []
    ans = []
    for num in sequence:
        if len(h) >= k:
            ans.append(heapq.heappop(h))
        heapq.heappush(h, num)
    while h:
        ans.append(heapq.heappop(h))

    return ans



def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
