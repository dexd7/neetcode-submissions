class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        dirs = [(-1,0),(1,0), (0,1), (0,-1)]
        curr_dist = 0
        while q:
            curr_dist +=1
            for i in range(len(q)):
                r,c = q.popleft()
                for dx,dy in dirs:
                    nr = r+dx
                    nc = c+dy
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and grid[nr][nc] != -1:
                        grid[nr][nc] = curr_dist
                        visited.add((nr,nc))
                        q.append((nr,nc))
        