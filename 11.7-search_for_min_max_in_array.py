import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    minsofar = A[0]
    maxsofar = A[0]
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            maxsofar = max(maxsofar, A[i])
            minsofar = min(minsofar, A[i+1])
        elif A[i+1] > A[i]:
            maxsofar = max(maxsofar, A[i+1])
            minsofar = min(minsofar, A[i])
    return MinMax(minsofar, maxsofar)



def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
