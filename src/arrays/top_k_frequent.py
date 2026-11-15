from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent elements in O(n log k) time."""
    if k <= 0:
        return []
    counts = Counter(nums)
    top_pairs = heapq.nlargest(k, counts.items(), key=lambda item: item[1])
    return [num for num, _ in top_pairs]
