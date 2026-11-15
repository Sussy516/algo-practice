from collections import deque


def shortest_grid_path(grid: list[list[int]]) -> int:
    """Return shortest 4-directional path length from (0, 0) to (R-1, C-1), or -1.

    0 represents open cells, 1 represents blocked cells.
    """
    if not grid or not grid[0]:
        return -1
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    if rows == 1 and cols == 1:
        return 0

    queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                if nr == rows - 1 and nc == cols - 1:
                    return dist + 1
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1
