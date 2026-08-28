class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dirs = [(0,-1),(0,1),(1,0),(-1,0)]
        def bfs(i,j):
            visited.add((i,j))
            q = deque()
            q.append((i,j))
            area = 1
            while q:
                r,c = q.popleft()
                for dr, dy in dirs:
                    newr, newc = r+dr, c+dy
                    if 0<=newr<ROWS and 0<=newc<COLS and (newr, newc) not in visited and grid[newr][newc] == 1:
                        area+=1
                        visited.add((newr, newc))
                        q.append((newr, newc))
            return area
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea