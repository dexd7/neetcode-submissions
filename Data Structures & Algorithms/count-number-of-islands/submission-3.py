class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def bfs(i, j):
            q = deque()
            q.append([i,j])
            visited.add((i,j))
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
                row, col = q.popleft()
                for dx,dy in dirs:
                    nrow = row+dx
                    ncol = col+dy
                    if (0<=nrow<ROWS and
                        0<=ncol<COLS and
                        (nrow,ncol) not in visited and 
                        grid[nrow][ncol] == '1'):
                        q.append([nrow,ncol])
                        visited.add((nrow,ncol))
        numIslands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == '1':
                    bfs(i,j)
                    numIslands += 1
        return numIslands