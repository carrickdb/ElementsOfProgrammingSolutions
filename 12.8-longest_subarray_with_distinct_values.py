from typing import List

from test_framework import generic_test

from collections import Counter
def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    left = 0
    longest = 0
    counts = Counter()
    for i, n in enumerate(A):
        counts[n] += 1
        while counts[n] > 1:
            counts[A[left]] -= 1
            left += 1
        longest = max(longest, i-left+1)
    return longest



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
