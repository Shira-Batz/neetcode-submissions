from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        ret = -1
        coords = [(r, c, 0) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 2]
        queue = deque(coords)
        minutes = 0
        while queue:
            r, c, m = queue.popleft()
            dir = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
            for cord in dir:
                i, j = cord
                if 0<=i<x and 0<=j<y and grid[i][j] == 1:
                    grid[i][j] = 2
                    queue.append((i, j, m+1))
                    minutes = m+1
        if not any(1 in row for row in grid):
            ret = minutes
        return ret