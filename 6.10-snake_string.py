from test_framework import generic_test


def snake_string(s: str) -> str:
    ans = []
    ans.append(s[1::4])
    ans.append(s[0::2])
    ans.append(s[3::4])
    return ''.join(ans)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
