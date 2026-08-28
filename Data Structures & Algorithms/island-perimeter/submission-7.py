class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    q.append((i,j))
                    break
            else:
                continue
            break

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            r,c = q.popleft()
            for dx, dy in dirs:
                newr, newc = r+dx, c+dy
                if 0<=newr<ROWS and 0<=newc<COLS:
                    if grid[newr][newc] == 1 and (newr, newc) not in visited:
                        visited.add((newr, newc))
                        q.append((newr, newc))
                    elif grid[newr][newc] == 0:
                        perimeter+=1
                else:
                    perimeter+=1
        return perimeter