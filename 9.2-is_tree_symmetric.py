from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if tree == None:
        return True
    s1,s2 = [tree],[tree]
    while s1 and s2:
        c1 = s1.pop()
        c2 = s2.pop()
        if c1.data != c2.data:
            return False
        if ((c1.right==None) ^ (c2.left==None)) != False:
            return False
        if c1.right != None:
            s1.append(c1.right)
            s2.append(c2.left)
        if ((c1.left==None) ^ (c2.right==None)) != False:
            return False
        if c1.left != None:
            s1.append(c1.left)
            s2.append(c2.right)

    return not s1 and not s2



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
