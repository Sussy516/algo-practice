def max_subarray(nums: list[int]) -> int:
    """Find the maximum contiguous subarray sum using Kadane's algorithm."""
    if not nums:
        raise ValueError("Input array must not be empty")
    current = best = nums[0]
    for value in nums[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best
