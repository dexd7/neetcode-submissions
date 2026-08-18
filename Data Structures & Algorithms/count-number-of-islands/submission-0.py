from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q = deque()
            q.append([r,c])
            visited.add((r,c))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            while q:
                row,col = q.popleft()
                for dx,dy in dirs:
                    if (0<=row+dx<ROWS and
                        0<=col+dy<COLS and 
                        (row+dx, col+dy) not in visited 
                        and grid[row+dx][col+dy] == '1'):
                        visited.add((row+dx,col+dy))
                        q.append([row+dx, col+dy])
        
        ROWS = len(grid)
        COLS = len(grid[0])
        numIslands = 0
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == '1':
                    numIslands+=1
                    bfs(i,j)

        return numIslands
        