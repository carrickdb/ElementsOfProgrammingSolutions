from test_framework import generic_test

import operator

def evaluate(expression: str) -> int:
    s = []
    ops = {
        "*" : operator.mul,
        "+": operator.add,
        "-": operator.sub,
        "/": operator.floordiv,
    }
    for ch in expression.split(','):
        if ch in ops:
            n1,n2 = s.pop(), s.pop()
            s.append(ops[ch](n2, n1))
        else:
            s.append(int(ch))

    if not s:
        return None
    return s[0]




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
