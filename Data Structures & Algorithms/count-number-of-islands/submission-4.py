class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        m,n = len(grid),len(grid[0])
        islands = 0
        queue = deque()

        queue.append((0,0))
        while queue:
            x,y = queue.popleft()

            if grid[x][y] == "1":
                islands+=1
                queue2 = deque()

                queue2.append((x,y))
                while queue2:
                    a,b = queue2.popleft()
                    for c,d in dirs:
                        if 0 <= a+c < m and 0 <= b+d < n:
                            if grid[a+c][b+d] == "1":
                                queue2.append((a+c,b+d))
                            elif grid[a+c][b+d] == "0":
                                queue.append((a+c,b+d))
                    grid[a][b] = 3

            elif grid[x][y] == "0":
                for c,d in dirs:
                    if 0 <= x+c < m and 0 <= y+d < n:
                        queue.append((x+c,y+d))
                grid[x][y] = 2
        return islands

        