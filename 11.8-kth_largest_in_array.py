from typing import List

from test_framework import generic_test

"""
[-4, 2, 3, 1]

"""
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    la = len(A)
    l,r = 0,la-1
    while l <= r:
        currI = (l+r)//2
        currval = A[currI]
        A[r], A[currI] = A[currI], A[r]
        p1,p2 = l,r-1
        while p1 <= p2:
            if A[p1] > currval:
                p1 += 1
            elif A[p2] < currval:
                p2 -= 1
            else:
                A[p1], A[p2] = A[p2], A[p1]
                p1 += 1
                p2 -= 1
        A[r], A[p1] = A[p1], A[r]
        if p1 == k-1:
            return currval
        if p1 < k-1:
            l = p1 + 1
        else:
            r = p1-1
    return A[l]


        

    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
