class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def addRooms(r,c):
            if (r,c) in visited or r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == -1:
                return
            q.append((r,c))
            visited.add((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c)) #dont forget to add in visited here because while doing bfs might reach same node and update its value since we dont check for 0 condition
        distance_so_far = 0
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                grid[row][col] = distance_so_far
                addRooms(row+1, col)
                addRooms(row-1,col)
                addRooms(row,col+1)
                addRooms(row,col-1)
            distance_so_far += 1
        
            