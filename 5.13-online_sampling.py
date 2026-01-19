import functools
from typing import Iterator, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

from random import random, randint

# Assumption: there are at least k elements in the stream.
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:
    s = []
    num_seen = 0
    """
    number of subsets item i is in:
    (n choose k) - (n-1 choose k) = (n-1 choose k-1)
    divide by total number of subsets to derive chances that i is in new subset:
    (n-1 choose k-1)/(n choose k) = (factorial stuff) = k/n
    """
    while True:
        try:
            num_seen += 1
            n = next(stream)
            if len(s) < k:
                s.append(n)
            else:
                randFloat = random()
                if randFloat < k/num_seen:
                    s[randint(0,len(s)-1)] = n
        except:
            break
    return s
    


@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(
            lambda:
            [online_random_sample(iter(stream), k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_sampling.py',
                                       'online_sampling.tsv',
                                       online_random_sample_wrapper))
