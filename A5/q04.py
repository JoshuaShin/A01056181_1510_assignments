"""
q04.py

A simple selection sort algorithm.
"""


# Joshua Shin
# A01056181
# April 15th 2019


import doctest


def selection_sort(numbers: list) -> list:
    """
    Sort the list in increasing order using selection sort algorithm.

    PARAM non-empty list of sortable items
    RETURN a sorted list in increasing order

    >>> selection_sort([3, 5, 1, 9, -4])
    [-4, 1, 3, 5, 9]
    """
    if len(numbers) == 0:
        raise ValueError("Cannot sort empty list!")
    else:
        numbers_copy = numbers[:]
        for i in range(len(numbers_copy)):
            min_index = numbers_copy.index(min(numbers_copy[i:]))
            numbers_copy[i], numbers_copy[min_index] = numbers_copy[min_index], numbers_copy[i]
        return numbers_copy


def main():
    doctest.testmod()
    print(selection_sort([3, 5, 1, 9, -4]))


if __name__ == "__main__":
    main()
