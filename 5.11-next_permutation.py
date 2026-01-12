from typing import List

from test_framework import generic_test

def next_permutation(perm: List[int]) -> List[int]:
    l = len(perm)
    pivot = l-2
    while pivot >= 0 and perm[pivot] >= perm[pivot+1]:
        pivot -= 1
    if pivot == -1:
        return []
    pivotVal = perm[pivot]
    print(pivot)
    swapIndex = 0
    for i in range(pivot+1, l):
        if perm[i] <= pivotVal:
            swapIndex = i-1
            break
        else:
            swapIndex = i
    print("swapIndex, perm[swapIndex]", swapIndex, perm[swapIndex])
    perm[pivot] = perm[swapIndex]
    perm[swapIndex] = pivotVal
    return perm[:pivot+1] + perm[pivot+1:][::-1]
    

# print(next_permutation([4, 2, 2, 4, 2]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
