import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    ans = Subarray(-1, -1)
    rev = {}
    for i,k in enumerate(keywords):
        rev[k] = i
    shortest = {}
    last_seen = {}
    for i,p in enumerate(paragraph):
        if p in rev:
            currI = rev[p]
            if currI == 0:
                shortest[currI] = 1
            elif currI-1 in shortest:
                prev_kw = keywords[currI-1]
                shortest[currI] = i - last_seen[prev_kw] + shortest[currI-1]
                if currI == len(keywords) - 1 and (ans.end - ans.start + 1 > shortest[currI] or ans == Subarray(-1, -1)):
                    ans = Subarray(i - shortest[currI]+1, i)
                    
            last_seen[p] = i
    return ans


# print(find_smallest_sequentially_covering_subset(["U", "o", "j", "M", "I", "N", "p", "y", "g", "p", "q", "u", "J", "t", "p", "Y", "l", "J", "K", "J", "u", "v", "W", "v", "J", "u", "Q", "m", "G", "D", "K", "D", "b", "g", "L", "N", "R", "D", "s", "i", "W", "i", "n", "c", "q", "D", "q", "s", "O", "f", "D", "N", "T", "S", "M", "i", "C", "o", "g", "t", "m", "T", "d", "c", "q", "t", "f", "f", "k", "l", "d", "U", "c", "H", "P", "P", "c", "v", "T", "G", "l", "D", "N", "Q", "T", "h", "H", "U", "H", "r", "v", "b", "V", "I", "U", "J", "u", "y", "J", "w", "z", "E", "E", "w", "y", "d", "e", "C", "P", "O", "Z", "o", "K", "n", "M", "b", "e", "a", "v", "O", "R", "m", "X", "q", "l", "p", "O", "c", "O", "H", "P", "i", "S", "R", "Z", "f", "l", "T", "a", "q", "Q", "P", "D", "P", "W", "a", "n", "a", "B", "H", "p", "x", "M", "n", "V", "M", "Y", "L", "N", "D", "T", "T", "G", "M", "s", "D", "z", "X", "u", "O", "A", "k", "w", "Z", "a", "m", "G", "G", "G", "X", "y", "q", "s", "W", "B", "m", "g", "K", "g", "F", "F", "C", "l", "m", "L", "A", "X", "O", "D", "X", "Z", "r", "g", "g", "u", "r", "m", "e", "r", "J", "A", "N", "K", "P", "e", "v", "a", "S", "J", "r", "L", "t", "Y", "g", "S", "T", "t", "V", "F", "n", "b", "A", "i", "h", "X", "H", "U", "X", "z", "z"], ["O", "R", "P", "m"]))

@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
