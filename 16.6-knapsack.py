import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    dp = [0 for _ in range(capacity+1)]
    for item in items:
        new_dp = [0]
        for curr_weight in range(capacity):
            item_weight, val = item
            with_item = 0
            weight_without_item = curr_weight - item_weight + 1
            if weight_without_item >= 0:
                with_item = val + dp[weight_without_item]
            new_dp.append(max(with_item, dp[curr_weight+1]))
        dp = new_dp
    return dp[-1]

# capacity = 130
# items = [[10, 99], [25,155], [40,220], [8,35], [30,120], [10,40], [65,320]]
# print(optimum_subject_to_capacity(items, capacity))

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
