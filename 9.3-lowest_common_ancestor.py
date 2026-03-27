import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    found = namedtuple('found', ('node0', 'node1', 'lca'))

    def rec(curr):
        if not curr:
            return found(node0=False, node1=False, lca=None)
        if curr==node0 and curr==node1:
            return found(node0=True, node1=True, lca=curr)
        if curr == node0:
            return found(node0=True, node1=False, lca=None)
        if curr==node1:
            return found(False, True, None)

        lres = rec(curr.left)
        rres = rec(curr.right)
        if ((lres.node0 and rres.node1) or (lres.node1 and rres.node0)) and lca==None:
            return found(node0=True, node1=True, lca=curr)        
        return found(node0=lres.node0 or rres.node0,
                     node1=lres.node1 or lres.node1,
                     lca=lres.lca if lres.lca!=None else rres.lca)

    return rec(tree).lca

    


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
