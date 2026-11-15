import unittest

from src.arrays.top_k_frequent import top_k_frequent
from src.design.trie import Trie
from src.graphs.number_of_islands import count_islands


class TestAdditionalProblems(unittest.TestCase):
    def test_top_k_frequent(self) -> None:
        self.assertEqual(set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)), {1, 2})
        self.assertEqual(top_k_frequent([5], 1), [5])
        self.assertEqual(top_k_frequent([1, 2], 0), [])

    def test_trie_operations(self) -> None:
        trie = Trie()
        trie.insert("cyber")
        trie.insert("cyberpunk")
        self.assertTrue(trie.search("cyber"))
        self.assertFalse(trie.search("cyb"))
        self.assertTrue(trie.starts_with("cyb"))
        self.assertTrue(trie.search("cyberpunk"))

    def test_count_islands(self) -> None:
        grid = [
            ["1", "1", "0", "0"],
            ["1", "0", "0", "1"],
            ["0", "0", "1", "1"],
        ]
        self.assertEqual(count_islands(grid), 2)
        self.assertEqual(count_islands([]), 0)
