class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0,-1),(0,1),(1,0),(-1,0)]
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            area = 1
            while q:
                r,c = q.popleft()
                for dr, dy in dirs:
                    newr, newc = r+dr, c+dy
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc] == 1:
                        area+=1
                        grid[newr][newc] = 0
                        q.append((newr, newc))
            return area
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea