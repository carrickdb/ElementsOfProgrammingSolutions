import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    l = len(s)
    p1,p2 = 0,l-1
    while p1 < p2:
        s[p1], s[p2] = s[p2], s[p1]
        p1 += 1
        p2 -= 1
    p1,p2 = 0,0
    while True:
        while p2 < l and s[p2] != ' ':
            p2 += 1
        end = p2
        p2 -= 1
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        while end < l and s[end] == ' ':
            end += 1
        if end >= l:
            break
        p1, p2 = end, end
        

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)
    executor.run(functools.partial(reverse_words, s_copy))
    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
