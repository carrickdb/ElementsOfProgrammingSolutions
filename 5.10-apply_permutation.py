from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    curr = 0
    l = len(perm)
    while curr < l:
        tmp = A[curr]
        while perm[curr] != curr:
            # tmp is redundant here; can just swap and you'll have the next
            # one available where you need it
            A[perm[curr]], tmp = tmp, A[perm[curr]]
            perm[curr], curr = curr, perm[curr]
        curr += 1
        



def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
