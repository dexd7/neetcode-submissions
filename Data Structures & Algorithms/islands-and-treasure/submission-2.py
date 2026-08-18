class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0: #to find all treasure chests and start multi-source bfs from there
                    q.append([i,j])
        curr_distance = 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        while q:
            curr_distance+=1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dx,dy in dirs:
                    nr,nc = r+dx, c+dy
                    if (0<=nr<ROWS and
                        0<=nc<COLS and
                        grid[nr][nc] == INF):
                        grid[nr][nc] = curr_distance
                        q.append([nr,nc])
        return 
                
