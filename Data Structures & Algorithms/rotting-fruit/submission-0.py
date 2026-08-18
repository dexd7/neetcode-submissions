class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fresh = 0
        def addTime(r,c):
            if r<0 or c<0 or r>=ROWS or c>= COLS or (r,c) in visited or grid[r][c] == 0:
                return
            visited.add((r,c))
            q.append((r,c))
            nonlocal fresh
            fresh-=1
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        minutes = 0
        while q and fresh>0:
            changed = False
            for i in range(len(q)):
                row,col = q.popleft()
                before = len(q)
                addTime(row+1,col)
                addTime(row-1,col)
                addTime(row,col+1)
                addTime(row,col-1)
                if len(q)>before:
                    changed = True
            if changed:
                minutes+=1
        return minutes if fresh == 0 else -1