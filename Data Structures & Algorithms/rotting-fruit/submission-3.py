from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        ret = -1
        coords = [(r, c, 0) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 2]
        queue = deque(coords)
        minutes = 0
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while queue:
            r, c, m = queue.popleft()
            for cord in directions:
                i, j = cord
                i+=r
                j+=c
                if 0<=i<x and 0<=j<y and grid[i][j] == 1:
                    grid[i][j] = 2
                    queue.append((i, j, m+1))
                    minutes = m+1
        if not any(1 in row for row in grid):
            ret = minutes
        return ret