import unittest
from pathlib import Path

from scripts.stats import collect_topic_counts
from src.design.lru_cache import LRUCache
from src.graphs.shortest_path_bfs import shortest_grid_path


class TestDesignAndGraphs(unittest.TestCase):
    def test_lru_cache(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        self.assertEqual(cache.get(1), 10)
        cache.put(3, 30)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 30)

    def test_shortest_grid_path(self) -> None:
        grid = [
            [0, 0, 1],
            [1, 0, 0],
            [1, 1, 0],
        ]
        self.assertEqual(shortest_grid_path(grid), 4)
        self.assertEqual(shortest_grid_path([[0, 1], [1, 0]]), -1)
        self.assertEqual(shortest_grid_path([[0]]), 0)

    def test_stats_counter(self) -> None:
        src_dir = Path(__file__).resolve().parent.parent / "src"
        counts = collect_topic_counts(src_dir)
        self.assertEqual(sum(counts.values()), 8)
