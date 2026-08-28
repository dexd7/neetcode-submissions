class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        distance = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dirs:
                    newr ,newc = r+dx, c+dy
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc] == INF:
                        grid[newr][newc] = distance
                        q.append((newr, newc))
            distance+=1
        