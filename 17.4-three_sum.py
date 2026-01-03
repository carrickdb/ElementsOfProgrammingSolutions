from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    la = len(A)
    for num in A:
        p1,p2 = 0, len(A) - 1
        while p1 <= p2:
            curr_sum = A[p1] + A[p2] + num
            if curr_sum < t:
                p1 += 1
            elif curr_sum > t:
                p2 -= 1
            else:
                return True
    return False




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
