from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    curr = tree
    ans = []
    prev = None
    while curr:
        if not curr.left and not curr.right:
            ans.append(curr.data)
            if not curr.parent:
                break
            prev = curr
            curr = curr.parent
        elif prev == curr.left:
            ans.append(curr.data)
            prev = curr
            if curr.right:
                curr = curr.right
            else:
                curr = curr.parent
        elif prev == curr.right:
            prev = curr
            curr = curr.parent
        elif not curr.left:
            ans.append(curr.data)
            prev = curr
            curr = curr.right
        else:
            prev = curr
            curr = curr.left
    return ans




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
