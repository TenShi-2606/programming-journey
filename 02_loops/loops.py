"""Stage 2 — Loops, counting, accumulation, and stopping conditions.

Run with: python3 02_loops/loops.py
"""


def sum_to_n(n: int) -> int:
    """Return 1 + 2 + ... + n. For n <= 0, return 0."""
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


def factorial(n: int) -> int:
    """Return n! for a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is defined here only for n >= 0.")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def multiplication_table(n: int, limit: int = 10) -> list[str]:
    """Build the multiplication table for n from 1 through limit."""
    return [f"{n} x {i} = {n * i}" for i in range(1, limit + 1)]


def first_multiple_over(limit: int, base: int = 7) -> int:
    """Use a while loop to find the first multiple of base strictly above limit."""
    if base <= 0:
        raise ValueError("base must be positive")
    candidate = limit + 1
    while candidate % base != 0:
        candidate += 1
    return candidate


if __name__ == "__main__":
    print("Sum from 1 to 5:", sum_to_n(5))          # 15
    print("5 factorial:", factorial(5))             # 120
    print("\n".join(multiplication_table(3, 5)))
    print("First multiple of 7 above 20:", first_multiple_over(20))  # 21

    # Practice:
    # 1. Write a function that counts how many even numbers are in a list.
    # 2. Make factorial work with a while loop instead.
    # 3. What happens if a while loop's condition never becomes false?
