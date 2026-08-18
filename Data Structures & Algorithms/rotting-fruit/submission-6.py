class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i,j])
                if grid[i][j] == 1:
                    fresh+=1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        minutes = 0
        while queue and fresh>0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dx,dy in dirs:
                    nr = r+dx
                    nc = c+dy
                    if (0<=nr<ROWS and
                        0<=nc<COLS and
                        grid[nr][nc] == 1):
                        grid[nr][nc] += 1
                        queue.append([nr,nc])
                        fresh-=1
            minutes+=1
        return minutes if fresh == 0 else -1