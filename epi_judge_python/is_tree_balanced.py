from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Optional


def height(node: Optional[BinaryTreeNode]) -> tuple[int, bool]:
    if not node:
        return 0, True

    # check if left child is balanced
    left, left_ok = height(node.left)
    if not left_ok:
        return 0, False

    # check if right child is balanced
    right, right_ok = height(node.right)
    if not right_ok:
        return 0, False

    # check heights
    new_height = max(left, right) + 1
    balanced = abs(left - right) < 2
    return new_height, balanced

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    _, balanced = height(tree)
    return balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
