import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    curr = node0
    h0 = 0
    while curr:
        curr = curr.parent
        h0 += 1
    h1 = 0
    curr = node1
    while curr:
        curr = curr.parent
        h1 += 1
    if h1 > h0:
        for _ in range(h1-h0):
            node1 = node1.parent
    else:
        for _ in range(h0-h1):
            node0 = node0.parent
    while node0 != node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0
    



@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
