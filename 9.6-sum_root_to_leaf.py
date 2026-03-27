from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:

    def rec(curr, partial_sum):
        if not curr:
            return 0
        next_sum = (partial_sum << 1) | curr.data
        if not curr.left and not curr.right:
            return next_sum
        rsum = rec(curr.right, next_sum)
        lsum = rec(curr.left, next_sum)
        return rsum+lsum

    return rec(tree, 0)


# tree = BinaryTreeNode(1)
# tree.left = BinaryTreeNode(0)
# tree.right = BinaryTreeNode(1)
# print(sum_root_to_leaf(tree))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
