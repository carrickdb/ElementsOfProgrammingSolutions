from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    p1 = L
    ll = 0
    while p1:
        ll+=1
        p1 = p1.next
    if not ll:
        return L
    k %= ll
    p1,p2 = L,L
    for _ in range(k):
        p1 = p1.next
    while p1 and p1.next:
        p1 = p1.next
        p2 = p2.next
    p1.next = L
    L = p2.next
    p2.next = None
    return L




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
