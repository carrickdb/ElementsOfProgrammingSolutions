from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    while i >= 0:
        A[i] = (A[i]+1) % 10
        if A[i] != 0:
            break
        i -= 1
    if A[0] == 0:
        A[0] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
