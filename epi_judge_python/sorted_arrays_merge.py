from heapq import heappop, heappush, heapify
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = []
    def push(values: List[int]) -> None:
        if values:
            pair = values[0], values[1:]
            heappush(heap, pair)

    for item in sorted_arrays:
        push(item)
    
    out = []
    while heap:
        head, tail = heappop(heap)
        push(tail)
        out.append(head)

    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
