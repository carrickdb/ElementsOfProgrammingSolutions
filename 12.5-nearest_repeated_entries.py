from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    h = {}
    ans = float("inf")
    for i,word in enumerate(paragraph):
        if word in h:
            ans = min(ans, i-h[word])
        h[word] = i
    if ans == float("inf"):
        return -1
    return ans




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
