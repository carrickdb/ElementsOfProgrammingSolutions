from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    currNum = 0
    ans = 0

    def rec(curr):
        if not curr:
            return
        nonlocal currNum
        nonlocal ans
        currNum <<= 1
        currNum |= curr.data
        # print(curr.data, currNum, ans)
        if not curr.left and not curr.right:
            # print("not curr.left and not curr.right")
            ans += currNum
            currNum >>= 1
            return
        # print(curr.data)
        rec(curr.left)
        rec(curr.right)
        currNum >>= 1
        # print(currNum)

    rec(tree)
    return ans


# tree = BinaryTreeNode(1)
# tree.left = BinaryTreeNode(0)
# tree.right = BinaryTreeNode(1)
# print(sum_root_to_leaf(tree))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
