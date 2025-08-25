from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    sign = ''
    if x < 0:
        sign = '-'
        x = -1 * x

    out = []
    # assert(x > 0)
    while x:
        out.append(chr(ord('0') + x % 10))
        x = x // 10
    
    out.append(sign)
    return ''.join(out[::-1])


def string_to_int(s: str) -> int:
    start = 0
    sign = 1
    if s[0] == '-':
        sign = -1
        start = 1
    elif s[0] == '+':
        start = 1

    out = 0
    for c in s[start:]:
        digit = ord(c) - ord('0')
        out = 10 * out + digit
    return sign * out


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
