import unittest

from src.dp.climbing_stairs import climb_stairs
from src.searching.binary_search import binary_search, lower_bound
from src.strings.valid_parentheses import is_valid_parentheses


class TestCoreTopics(unittest.TestCase):
    def test_valid_parentheses(self) -> None:
        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertTrue(is_valid_parentheses("{[()]}"))
        self.assertFalse(is_valid_parentheses("(]"))
        self.assertFalse(is_valid_parentheses("((("))

    def test_binary_search_and_lower_bound(self) -> None:
        arr = [1, 3, 5, 5, 7, 9]
        self.assertEqual(binary_search(arr, 7), 4)
        self.assertEqual(binary_search(arr, 4), -1)
        self.assertEqual(lower_bound(arr, 5), 2)
        self.assertEqual(lower_bound(arr, 10), 6)

    def test_climb_stairs(self) -> None:
        self.assertEqual(climb_stairs(0), 1)
        self.assertEqual(climb_stairs(1), 1)
        self.assertEqual(climb_stairs(5), 8)
        with self.assertRaises(ValueError):
            climb_stairs(-1)
