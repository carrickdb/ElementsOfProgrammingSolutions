from test_framework import generic_test
from itertools import groupby

def look_and_say(n: int) -> str:
    curr = ["1"]
    for i in range(n-1):
        new = []
        for val, group in groupby(curr):
            new.extend([str(len(list(group))), val])
        curr = new
    return ''.join(curr)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
