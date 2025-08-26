from typing import Callable, List

from test_framework import generic_test


def advance(values: List[int], i: int, check: Callable[[int], bool]) -> int:
    while i != len(values) and check(values[i]):
        i += 1
    return i

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    i, j = 0, 0
    out = []
    while i != len(A) and j != len(B):
        left, right = A[i], B[j]
        if left == right:
            out.append(left)
            i = advance(A, i, lambda x: x == left)
            j = advance(B, j, lambda x: x == right)
        elif left < right:
            i = advance(A, i, lambda x: x < right)
        else:
            j = advance(B, j, lambda x: x < left)

    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
