from test_framework import generic_test

from functools import reduce

def rabin_karp(text: str, search: str) -> int:
    def convert(ch):
        return ord(ch) - ord(' ')

    base = 95
    hashs = reduce(lambda h, curr: h*base+convert(curr), search, 0)
    ls = len(search)
    lt = len(text)
    hasht = reduce(lambda h, curr: h*base+convert(curr), text[:ls], 0)
    i = ls
    while True:
        if hashs==hasht:
            return i-ls
        if i>=len(text):
            break
        hasht -= convert(text[i-ls])*(base**(ls-1))
        hasht *= base
        hasht += convert(text[i])
        i += 1
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
