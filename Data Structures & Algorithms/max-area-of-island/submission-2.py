class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(row, col):
            visited.add((row,col))
            q = deque()
            q.append((row,col))
            dirs = [(-1,0), (1,0), (0,1), (0,-1)]
            area = 1
            while q:
                r, c = q.popleft()
                for dx,dy in dirs:
                    nr = r+dx
                    nc = c+dy
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and grid[nr][nc] == 1:
                        area +=1
                        q.append((nr,nc))
                        visited.add((nr,nc))
            return area 
        visited = set()
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j]:
                    maxArea = max(maxArea,bfs(i,j))
        return maxArea