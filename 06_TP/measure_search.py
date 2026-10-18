"""TP — Compare empirical search times.

Run from the repository root:
    python3 06_TP/measure_search.py

This experiment is illustrative: timings depend on the computer, Python version,
and workload. Binary search is run on a sorted list.
"""
from time import perf_counter


def linear_search(values: list[int], target: int) -> int:
    """Return target's index, or -1 if it is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: list[int], target: int) -> int:
    """Search a sorted list in logarithmic time."""
    left, right = 0, len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def time_call(function, values: list[int], target: int, repeats: int = 100) -> float:
    """Return average elapsed seconds across repeated calls."""
    start = perf_counter()
    for _ in range(repeats):
        function(values, target)
    return (perf_counter() - start) / repeats


def main() -> None:
    sizes = [100, 1_000, 10_000, 100_000]
    print(f"{'n':>8} {'linear (ms)':>14} {'binary (ms)':>14}")
    for size in sizes:
        values = list(range(size))
        # Target at the end gives linear search a demanding case.
        target = size - 1
        linear_ms = time_call(linear_search, values, target) * 1_000
        binary_ms = time_call(binary_search, values, target) * 1_000
        print(f"{size:8d} {linear_ms:14.6f} {binary_ms:14.6f}")


if __name__ == "__main__":
    main()
