class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(i, j):
            q = deque()
            visited.add((i, j))
            q.append((i, j))
            while q:
                r, c = q.popleft()
                for dx, dy in dirs:
                    newr, newc = r+dx, c+dy
                    if 0<=newr<ROWS and 0<=newc<COLS and (newr, newc) not in visited and grid[newr][newc] == '1':
                        visited.add((newr, newc))
                        q.append((newr, newc))
                    

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == '1':
                    bfs(i, j)
                    num_islands+=1
        return num_islands