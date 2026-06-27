class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        m,n = len(grid),len(grid[0])
        islands = 0

        def bfs(r,c):
            que = deque()
            que.append((r,c))
            grid[r][c] = "0"
            while que:
                x,y = que.popleft()
                for a,b in dirs:
                    if 0 <= x+a < m and 0 <= y+b < n and grid[x+a][y+b] == "1":
                        que.append((x+a,y+b))
                        grid[x+a][y+b] = "0"

        for i in range (0,m):
            for j in range (0,n):
                if (grid[i][j] == "1"):
                    islands+=1
                    bfs(i,j)
        return islands


        