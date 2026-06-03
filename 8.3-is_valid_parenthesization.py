from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    parens = {'{': '}', '[': ']', '(': ')'}
    for ch in s:
        if ch in parens:
            stack.append(parens[ch])
        else:
            if not stack or stack[-1] != ch:
                return False
            stack.pop()
    return not stack

        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
