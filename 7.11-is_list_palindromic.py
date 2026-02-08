from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True
    p1,p2 = L,L
    prev = None
    even = False
    while p2 and p2.next:
        # print(p1.data, p2.data)
        p2 = p2.next
        if not p2 or not p2.next:
            even = True
            break
        # 0 1 2 3
        # <a<b c>d>e
        # <a<b<c d>e>f
        p2 = p2.next
        n = p1.next
        p1.next = prev
        prev = p1
        p1 = n
    p2 = p1.next
    if even:
        p1.next = prev
    else:
        p1 = prev
    # print(p1.data, p2.data)
    while p1 and p2:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
