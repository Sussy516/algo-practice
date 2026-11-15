import unittest

from src.arrays.max_subarray import max_subarray
from src.arrays.merge_intervals import merge_intervals
from src.arrays.two_sum import two_sum


class TestArrays(unittest.TestCase):
    def test_two_sum(self) -> None:
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 10)

    def test_max_subarray(self) -> None:
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_subarray([-5, -2, -9]), -2)
        with self.assertRaises(ValueError):
            max_subarray([])

    def test_merge_intervals(self) -> None:
        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertEqual(merge_intervals([[4, 5], [1, 4]]), [[1, 5]])
        self.assertEqual(merge_intervals([]), [])
