"""Stage 4 — Functions, parameters, return values, and modularity.

Run with: python3 04_functions/modularity.py
"""


def is_prime(number: int) -> bool:
    """Return True when number is prime, otherwise False."""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def count_vowels(text: str) -> int:
    """Count vowels in a string, ignoring case."""
    vowels = "aeiouy"
    return sum(1 for character in text.lower() if character in vowels)


def average(numbers: list[float]) -> float:
    """Return the average; raise an error for an empty list."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)


def run_demo() -> None:
    """Keep the demonstration separate from reusable function definitions."""
    print("Is 17 prime?", is_prime(17))
    print("Vowels in 'Algorithmique':", count_vowels("Algorithmique"))
    print("Average:", average([10, 12, 16]))


if __name__ == "__main__":
    run_demo()

    # Practice:
    # 1. Write a function that converts Celsius to Fahrenheit.
    # 2. Write a function that returns the minimum of a list.
    # 3. Explain why local variables inside a function do not automatically
    #    exist outside that function.
