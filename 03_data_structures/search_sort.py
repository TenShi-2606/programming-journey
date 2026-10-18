"""Stage 3 — Lists, matrices, searching, and sorting.

Run with: python3 03_data_structures/search_sort.py
Binary search requires a sorted list.
"""


def linear_search(values: list[int], target: int) -> int:
    """Return the index of target, or -1 when it is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(sorted_values: list[int], target: int) -> int:
    """Find target in ascending sorted_values in O(log n) time; return index or -1."""
    left = 0
    right = len(sorted_values) - 1

    while left <= right:
        middle = (left + right) // 2
        if sorted_values[middle] == target:
            return middle
        if sorted_values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def selection_sort(values: list[int]) -> list[int]:
    """Return a sorted copy using selection sort."""
    result = values.copy()
    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result


def bubble_sort(values: list[int]) -> list[int]:
    """Return a sorted copy using bubble sort."""
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


def matrix_sum(matrix: list[list[int]]) -> int:
    """Return the sum of all values in a rectangular matrix."""
    return sum(value for row in matrix for value in row)


if __name__ == "__main__":
    numbers = [8, 3, 6, 1, 5]
    ordered = selection_sort(numbers)
    print("Original:", numbers)
    print("Selection sort:", ordered)
    print("Bubble sort:", bubble_sort(numbers))
    print("Linear search for 6:", linear_search(numbers, 6))
    print("Binary search for 6:", binary_search(ordered, 6))
    print("Missing value:", binary_search(ordered, 99))
    print("Matrix sum:", matrix_sum([[1, 2, 3], [4, 5, 6]]))  # 21

    # Practice:
    # 1. Trace binary search on [1, 3, 5, 6, 8] looking for 6.
    # 2. Count comparisons made by linear search and binary search.
    # 3. Explain why binary search is not reliable on an unsorted list.
    # 4. Add a function that returns the largest value in a matrix.
