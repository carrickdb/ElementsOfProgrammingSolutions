import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    l = len(s)
    p1,p2 = 0,0
    new_size = 0
    while p1 < size and p2 < size:
        if s[p2] == "b":
            p2 += 1
            continue
        s[p1] = s[p2]
        p2 += 1
        new_size += 1
        p1 += 1
    final_size = sum(2 if s[i]=="a" else 1 for i in range(new_size))
    # print(new_size)
    p1,p2 = new_size-1, final_size-1
    while p1 >= 0 and p2 >= 0:
        if s[p1] == "a":
            s[p2] = "d"
            p2 -= 1
            s[p2] = "d"
        else:
            s[p2] = s[p1]
        p2 -= 1
        p1 -= 1
    return final_size

# print(replace_and_remove(6, ["b", "d", "c", "a", "b", "a"]))
# print(replace_and_remove(4, ["a", "b", "a", "d", "b"]))
# print(replace_and_remove(4, ["c", "b", "a", "c", "d", "b"]))

# print(replace_and_remove(4, ["a", "b", "a", "d", "b"]))
# print(replace_and_remove(2, ["b", "b"]))
# print(replace_and_remove(1, ["b", "b"]))
# print(replace_and_remove(4, ["b", "a", "a", "d", "c"]))

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
