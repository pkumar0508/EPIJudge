from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    counts = {}
    for letter in letter_text:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1

    for letter in magazine_text:
        if letter not in counts:
            continue

        counts[letter] -=1
        if not counts[letter]:
            del counts[letter]
        if not counts:
            break

    return not counts


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
