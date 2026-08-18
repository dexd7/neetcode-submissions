class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        q = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
                    break
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        perimeter = 0
        while q:
            r,c = q.popleft()
            for dx,dy in dirs:
                newr = r+dx
                newc = c+dy
                if (0<=newr<ROWS  and
                    0<=newc<COLS):
                    if ((newr,newc) not in visited and
                    grid[newr][newc] == 1):
                        q.append((newr,newc))
                        visited.add((newr,newc))
                    elif grid[newr][newc] == 0:
                        perimeter+=1
                else:
                    perimeter+=1
        return perimeter
            

                    
