from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    n = 0
    for c in num_as_string[num_as_string[0] in '-+':]:
        n *= b1
        n += int(c, 16)
    sl = []
    while True:
        curr = format(n%b2, 'X')
        sl.append(curr)
        n //= b2
        if n == 0:
            break
    if num_as_string[0] == "-":
        sl.append("-")
    return ''.join(sl[::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
