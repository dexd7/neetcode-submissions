class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            while queue:
                row,col = queue.popleft()
                for dx,dy in dirs:
                    nrow,ncol = row+dx,col+dy
                    if (nrow<ROWS and ncol<COLS and
                        nrow>=0 and ncol>=0 and
                        (nrow,ncol) not in visited and
                        grid[nrow][ncol] == '1'):
                        visited.add((nrow,ncol))
                        queue.append((nrow,ncol))
        visited = set()
        numIslands=0
        for i in range(ROWS):
            for j in range(COLS):
                if ((i,j) not in visited and grid[i][j] == '1'):
                    bfs(i,j)
                    numIslands+=1
        return numIslands
        