class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_fruits = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    total_fruits+=1
        if total_fruits == 0:
            return 0
        minutes_taken = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        while q:
            rotted_this_round = 0
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dirs:
                    newr, newc = r+dx, c+dy
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc] == 1:
                        rotted_this_round = 1
                        grid[newr][newc]+=1
                        total_fruits-=1
                        q.append((newr, newc))
            if rotted_this_round:
                minutes_taken+=1
        return minutes_taken if total_fruits == 0 else -1
        

        