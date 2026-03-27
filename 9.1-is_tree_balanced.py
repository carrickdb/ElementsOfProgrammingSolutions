from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    def balanced(curr):
        if not curr:
            return True, 0
        rbalanced, rh = balanced(curr.right)
        lbalanced, lh = balanced(curr.left)
        if not rbalanced or not lbalanced:
            return False, 0
        return abs(rh-lh) <= 1, max(rh, lh)+1

    b, _ = balanced(tree)
    return b

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
