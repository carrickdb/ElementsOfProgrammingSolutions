import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    l = len(s)
    p1,p2 = 0,0
    while p2 < size:
        if s[p2] == "b":
            p2 += 1
            continue
        s[p1] = s[p2]
        p2 += 1
        p1 += 1
    final_size = sum(2 if s[i]=="a" else 1 for i in range(p1))
    p1,p2 = p1-1, final_size-1
    while p1 >= 0:
        if s[p1] == "a":
            s[p2] = "d"
            p2 -= 1
            s[p2] = "d"
        else:
            s[p2] = s[p1]
        p2 -= 1
        p1 -= 1
    return final_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
