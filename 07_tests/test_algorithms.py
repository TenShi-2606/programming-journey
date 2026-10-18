"""Automated regression tests for the learning algorithms.

Run from the repository root:
    python3 -m unittest discover -s 07_tests -v
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from importlib.util import module_from_spec, spec_from_file_location


def load_module(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


conditions = load_module("conditions", "01_fundamentals/conditions.py")
loops = load_module("loops", "02_loops/loops.py")
search_sort = load_module("search_sort", "03_data_structures/search_sort.py")
modularity = load_module("modularity", "04_functions/modularity.py")


class TestConditions(unittest.TestCase):
    def test_number_description(self):
        self.assertEqual(conditions.describe_number(7), "7 is positive and odd.")
        self.assertEqual(conditions.describe_number(-4), "-4 is negative and even.")
        self.assertEqual(conditions.describe_number(0), "0 is zero and even.")

    def test_score_validation(self):
        self.assertEqual(conditions.calculate_grade(9), "Fail")
        self.assertEqual(conditions.calculate_grade(10), "Pass")
        self.assertIn("Invalid", conditions.calculate_grade(21))

    def test_access_requires_both_conditions(self):
        self.assertTrue(conditions.can_access(18, True))
        self.assertFalse(conditions.can_access(17, True))
        self.assertFalse(conditions.can_access(18, False))


class TestLoops(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(loops.sum_to_n(5), 15)
        self.assertEqual(loops.sum_to_n(0), 0)

    def test_factorial(self):
        self.assertEqual(loops.factorial(0), 1)
        self.assertEqual(loops.factorial(5), 120)
        with self.assertRaises(ValueError):
            loops.factorial(-1)

    def test_first_multiple_over(self):
        self.assertEqual(loops.first_multiple_over(20), 21)


class TestDataStructures(unittest.TestCase):
    def test_searches(self):
        values = [1, 3, 5, 6, 8]
        self.assertEqual(search_sort.linear_search(values, 6), 3)
        self.assertEqual(search_sort.binary_search(values, 6), 3)
        self.assertEqual(search_sort.binary_search(values, 99), -1)

    def test_sorts_do_not_mutate_input(self):
        values = [8, 3, 6, 1, 5]
        self.assertEqual(search_sort.selection_sort(values), [1, 3, 5, 6, 8])
        self.assertEqual(search_sort.bubble_sort(values), [1, 3, 5, 6, 8])
        self.assertEqual(values, [8, 3, 6, 1, 5])

    def test_matrix_sum(self):
        self.assertEqual(search_sort.matrix_sum([[1, 2, 3], [4, 5, 6]]), 21)


class TestFunctions(unittest.TestCase):
    def test_prime(self):
        self.assertFalse(modularity.is_prime(1))
        self.assertTrue(modularity.is_prime(2))
        self.assertTrue(modularity.is_prime(17))
        self.assertFalse(modularity.is_prime(21))

    def test_vowels_and_average(self):
        self.assertEqual(modularity.count_vowels("Algorithmique"), 6)
        self.assertEqual(modularity.average([10, 12, 16]), 12.666666666666666)
        with self.assertRaises(ValueError):
            modularity.average([])


if __name__ == "__main__":
    unittest.main()
