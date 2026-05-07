from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from itertools import tee
from collections import Counter

def find_missing_element(stream: Iterator[int]) -> int:
    s1, s2 = tee(stream)
    counter = Counter()
    for ip in s1:
        counter[ip >> 16] += 1
    
    for prefix, count in counter.items():
        if count < 2**16:
            break
    
    ips = set()
    for ip in s2:
        if (ip >> 16) != prefix:
            continue
        ips.add(ip & ((1<<16) - 1))
    
    for i in range(2**16):
        if i not in ips:
            return (prefix << 16) | i


    


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
