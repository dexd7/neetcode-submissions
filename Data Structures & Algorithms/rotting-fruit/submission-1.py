class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        rotten_starts = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_starts.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        directions = [(-1,0), (1, 0), (0, 1) ,(0, -1)]
        total_minutes = 0
        while rotten_starts and fresh>0:
            total_minutes+=1
            for _ in range(len(rotten_starts)):
                row,col = rotten_starts.popleft()
                for dx,dy in directions:
                    nr = row+dx
                    nc = col+dy
                    if (0<=nr<ROWS and
                        0<=nc<COLS and
                        grid[nr][nc] == 1):
                        rotten_starts.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh-=1
        return total_minutes if fresh == 0 else -1

