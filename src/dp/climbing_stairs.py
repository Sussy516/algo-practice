def climb_stairs(n: int) -> int:
    """Count distinct ways to climb n steps taking 1 or 2 steps at a time."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
