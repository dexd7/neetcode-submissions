class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        starting_points = deque()
        fresh_fruits = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    starting_points.append((r,c))
                if grid[r][c] == 1:
                    fresh_fruits += 1
        if fresh_fruits == 0:
            return 0
        minutes_taken = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while starting_points:
            flag_rotten = 0
            for _ in range(len(starting_points)):
                r, c = starting_points.popleft()
                for dx, dy in dirs:
                    newr, newc = r+dx, c+dy
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc] == 1:
                        grid[newr][newc] += 1
                        fresh_fruits-=1
                        flag_rotten = 1
                        starting_points.append((newr, newc))
            if flag_rotten:
                minutes_taken += 1
        return minutes_taken if fresh_fruits == 0 else -1
