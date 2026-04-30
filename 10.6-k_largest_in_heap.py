from typing import List

from test_framework import generic_test, test_utils

import heapq

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    h = []
    ans = []
    while len(ans) < k:
        if h:
            nextVal, nextI = heapq.heappop(h)
            ans.append(-nextVal)
            child = 2*nextI + 1
            if child >= len(A):
                continue
            heapq.heappush(h, (-A[child], child))
            child += 1
            if child >= len(A):
                continue
            heapq.heappush(h, (-A[child], child))
        else:
            heapq.heappush(h, (-A[0], 0))

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
