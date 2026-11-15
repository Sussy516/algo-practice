def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge all overlapping [start, end] intervals in O(n log n) time."""
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda pair: (pair[0], pair[1]))
    merged: list[list[int]] = [ordered[0][:]]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
