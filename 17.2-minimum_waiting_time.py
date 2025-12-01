from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    times = sorted(service_times)
    t = 0
    ls = len(service_times)
    for i in range(ls-1):
        t += times[i] * (ls - i - 1)
    return t


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
