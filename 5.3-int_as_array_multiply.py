from typing import List

from test_framework import generic_test

def zero(n):
    return len(n) == 1 and n[0] == 0

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if zero(num1) or zero(num2):
        return [0]
    ans = []
    p = 0
    neg = (num1[0] < 0) ^ (num2[0] < 0)
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    for n1 in reversed(num1):
        curr = []
        carry = 0
        for n2 in reversed(num2):
            res = n1*n2 + carry
            curr.append(res % 10)
            carry = res //10
        if carry:
            curr.append(carry)
        # print(f"{curr=}")
        carry = 0
        for i in range(len(curr)):
            if i+p >= len(ans):
                ans.append(curr[i]+carry)
            else:
                s = ans[i+p] + curr[i] + carry
                ans[i+p] = s%10
                carry = s//10
        p += 1
        # print(ans[::-1])
    if neg:
        ans[-1] *= -1
    return ans[::-1]


# print(multiply([2], [9]))
# print(multiply([-2], [9]))
# print(multiply([3,4],[5]))  # 170
# print(multiply([3,4],[4,5]))  # 1530
# print(multiply([3,4,6],[4,5]))  #15,570

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
