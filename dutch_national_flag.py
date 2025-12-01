import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    l, e, g, p = 0,0,len(A), A[pivot_index]
    while e < g:
        c = A[e]
        if c == p:
            e += 1
        elif c < p:
            A[l], A[e] = c, A[l]
            l+=1
            e += 1
        else:
            g -= 1
            A[g], A[e] = c, A[g]

A = [1, 0, 2, 0, 2, 1, 2, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 2, 1, 0, 2, 1, 2, 0, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 2, 2, 0, 1, 0, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 2, 1, 2, 2, 1, 0, 1, 2, 2, 1, 2, 2, 1, 1, 2, 0, 1, 0, 1, 2, 0, 2, 1, 2, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0]
dutch_flag_partition(101, A)
print(A)



    # p = A[pivot_index]
    # l, h = 0, len(A)-1
    # s1, s2 = l, h
    # while l < h:
    #     if A[l] < p:
    #         l += 1
    #     elif A[h] > p:
    #         h -= 1
    #     elif A[h] < p and A[l] > p:
    #         tmp = A[h]
    #         A[h] = A[l]
    #         A[l] = tmp
    #         h += 1
    #         l -= 1
    #     elif A[l] == p:
    #         if s1 <= l:
    #             s1 = l+1
    #         while s1 < s2 and A[s1] == p:
    #             s1 += 1
    #         if s1 >= s2:
    #             break
    #         A[l] = A[s1]
    #         A[s1] = p
    #     else:
    #         if s2 >= h:
    #             s2 = h-1
    #         while s2 > s1 and A[s2] == p:
    #             s2 -= 1
    #         if s2 <= s1:
    #             break
    #         A[h] = A[s2]
    #         A[s2] = p



@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
