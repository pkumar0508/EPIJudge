from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def insert_after(node: ListNode, insert: ListNode) -> None:
    insert.next = node.next
    node.next = insert


def pop_front(node: ListNode) -> tuple[ListNode, Optional[ListNode]]:
    tail = node.next
    node.next = None
    return node, tail


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode()
    current = sentinel

    while L1 and L2:
        if L1.data < L2.data:
            node, L1 = pop_front(L1)
        else:
            node, L2 = pop_front(L2)

        insert_after(current, node)
        current = current.next

    if L1:
        current.next = L1
    if L2:
        current.next = L2

    return sentinel.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
