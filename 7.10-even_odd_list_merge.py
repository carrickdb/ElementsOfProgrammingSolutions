from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    even = True
    evens, odds = ListNode(0), ListNode(1)
    currEven, currOdd = evens, odds
    curr = L
    while curr:
        if even:
            currEven.next = curr
            currEven = currEven.next
            curr = curr.next
            currEven.next = None
        else:
            currOdd.next = curr
            currOdd = currOdd.next
            curr = curr.next
            currOdd.next = None
        even = not even
    currEven.next = odds.next
    return evens.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
