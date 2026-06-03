from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    ans = ListNode(0)
    anshead = ans
    carry = 0
    while L1 or L2:
        # print(L1.data)
        curr = carry
        if L1:
            curr += L1.data
            L1 = L1.next
        if L2:
            curr += L2.data
            L2 = L2.next
        if curr >= 10:
            carry = 1
            curr %= 10
        else:
            carry = 0
        ans.next = ListNode(curr)
        ans = ans.next
    if carry:
        ans.next = ListNode(carry)

    return anshead.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
