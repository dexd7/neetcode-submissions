class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def bfs(i,j):
            q = deque()
            visited.add((i,j))
            q.append([i,j])
            dirs = [[0,1], [0,-1], [1, 0], [-1, 0]]
            areaIsland = 1
            while q:
                r, c = q.popleft()
                for dx,dy in dirs:
                    nr = r+dx
                    nc = c+dy
                    if (0<=nr<ROWS and 
                        0<=nc<COLS and
                        (nr,nc) not in visited and
                        grid[nr][nc] == 1):
                        areaIsland += 1
                        visited.add((nr, nc))
                        q.append([nr, nc])
            return areaIsland
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea
