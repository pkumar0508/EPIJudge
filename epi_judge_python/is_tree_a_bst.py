from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Iterator, Optional

def inorder(tree: Optional[BinaryTreeNode]) -> Iterator[BinaryTreeNode]:
    if tree:
        yield from inorder(tree.left)
        yield tree
        yield from inorder(tree.right)

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    nodes = inorder(tree)

    # process nodes pairwise to check sortedness
    left = next(nodes, None)
    right = next(nodes, None)

    while left and right:
        if left.data > right.data:
            return False
        # shift pairwise window
        left = right
        right = next(nodes, None)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
