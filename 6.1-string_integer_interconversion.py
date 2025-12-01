from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    sl = []
    orig = x
    x = abs(x)
    while x > 0:
        sl.append(chr(ord("0") + (x%10)))
        x //= 10
    if orig < 0:
        sl.append("-")
    s = ''.join(sl[::-1])
    return s

def string_to_int(s: str) -> int:
    n = 0
    place = 1
    for i in range(len(s)-1,-1,-1):
        if s[i] == "-":
            n = -n
        elif s[i] == "+":
            break
        else:
            n += (ord(s[i]) - ord("0")) * place
            place *= 10
    return n

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
