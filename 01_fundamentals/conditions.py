"""Stage 1 — Variables, types, booleans, and conditions.

Run with: python3 01_fundamentals/conditions.py
These are learning examples; change the values and predict the output first.
"""


def describe_number(number: int) -> str:
    """Return whether a number is positive, negative, or zero, and its parity."""
    if number > 0:
        sign = "positive"
    elif number < 0:
        sign = "negative"
    else:
        sign = "zero"

    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    return f"{number} is {sign} and {parity}."


def calculate_grade(score: float) -> str:
    """Classify a score from 0 to 20."""
    if not 0 <= score <= 20:
        return "Invalid score: enter a value from 0 to 20."
    if score >= 16:
        return "Very good"
    elif score >= 14:
        return "Good"
    elif score >= 12:
        return "Fairly good"
    elif score >= 10:
        return "Pass"
    else:
        return "Fail"


def can_access(age: int, has_permission: bool) -> bool:
    """Access is allowed only if the person is at least 18 and has permission."""
    return age >= 18 and has_permission


if __name__ == "__main__":
    print(describe_number(7))
    print(describe_number(-4))
    print(calculate_grade(15))
    print("Access allowed:", can_access(20, True))

    # Try these yourself:
    # 1. Change the numbers and scores above.
    # 2. Add a function that returns the largest of three numbers.
    # 3. Explain why can_access(17, True) returns False.
