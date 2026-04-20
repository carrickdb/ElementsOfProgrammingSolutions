from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    ll = len(preorder)
    if ll == 0:
        return None
    m = {}
    for i,n in enumerate(inorder):
        m[n] = i
    def rec(preorderI, inorder_start, inorder_end):
        if preorderI == ll:
            return None, preorderI
        if inorder_start >= inorder_end:
            return None, preorderI
        currVal = preorder[preorderI]
        curr = BinaryTreeNode(currVal)
        currI = m[currVal]
        curr.left, newPreorderI = rec(preorderI+1, inorder_start, currI)
        curr.right, newPreorderI = rec(newPreorderI, currI+1, inorder_end)
        return curr, newPreorderI

    root, _ = rec(0, 0, ll)
    return root


# print(binary_tree_from_preorder_inorder(["H", "B", "F", "E", "A", "C", "D", "G", "I"], ["F", "B", "A", "E", "H", "C", "D", "I", "G"]))
# print(binary_tree_from_preorder_inorder(["B"], ["B"]))
"""
["F", "B", "A", "E", "H", "C", "D", "I", "G"]
["F", "B", "A", "E",]
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
