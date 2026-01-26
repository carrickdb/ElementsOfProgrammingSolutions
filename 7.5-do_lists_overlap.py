import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_entry(node):
    t,r = node, node
    while r:
        r = r.next
        if not r:
            break
        r = r.next
        t = t.next
        if r is t:
            p = node
            while not p is t:
                p = p.next
                t = t.next
            return p
    return None

def get_tail(n):
    while n:
        if not n.next:
            return n
        n = n.next

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    if l0 is None or l1 is None:
        return None
    entry1 = get_entry(l0)
    entry2 = get_entry(l1)
    if ((entry1==None) ^ (entry2==None)) == True:
        return None
    if entry1 is None:
        tail1 = get_tail(l0)
        tail2 = get_tail(l1)
        if tail1 is tail2:
            return tail1
        return None
    curr = entry1
    while curr is not entry2:
        curr = curr.next
        if curr is entry1:
            return None
    return entry1


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
