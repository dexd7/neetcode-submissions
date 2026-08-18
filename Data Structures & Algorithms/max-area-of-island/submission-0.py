class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(i,j):
            area = 1
            q = deque()
            q.append((i,j))
            visited.add((i,j))
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                row, col = q.popleft()
                for dx,dy in dirs:
                    nrow = row+dx
                    ncol = col+dy
                    if (nrow>=0 and ncol>=0 and nrow<ROWS and ncol<COLS and (nrow,ncol) not in visited and grid[nrow][ncol] == 1):
                        visited.add((nrow,ncol))
                        q.append((nrow,ncol))
                        area +=1
            return area
        visited = set()
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == 1:
                    maxArea = max(maxArea,bfs(i,j))
        return maxArea