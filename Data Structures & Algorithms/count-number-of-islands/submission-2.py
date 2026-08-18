class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        
        def bfs(i,j):
            q = deque()
            visited.add((i,j))
            q.append((i,j))
            dirs = [[0,-1],[0,1],[1,0],[-1,0]]
            while q:
                r,c = q.popleft()
                for dx,dy in dirs:
                    nr,nc = r+dx,c+dy
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and grid[nr][nc] == '1':
                        q.append((nr,nc))
                        visited.add((nr,nc))


        visited = set()
        numIslands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == '1':
                    bfs(i,j)
                    numIslands+=1
        return numIslands
                

