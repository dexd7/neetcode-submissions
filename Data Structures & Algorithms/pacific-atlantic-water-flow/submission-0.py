class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        pacific_starts = []
        for i in range(ROWS):
            pacific_starts.append((i,0))
        for j in range(COLS):
            pacific_starts.append((0,j))        
        atlantic_starts = []
        for i in range(ROWS):
            atlantic_starts.append((i,COLS-1))
        for j in range(COLS):
            atlantic_starts.append((ROWS-1, j))
        dirs = [(1,0),(-1,0),(0,-1), (0, 1)]
        def multi_bfs(starts):
            q = deque(starts)
            visited = set(starts)
            while q:
                r, c = q.popleft()
                for dx,dy in dirs:
                    newr,newc = r+dx,c+dy
                    if ( (newr, newc) not in visited and
                         0<=newr<ROWS and
                         0<=newc<COLS and
                         heights[newr][newc] >= heights[r][c]):
                         q.append((newr,newc))
                         visited.add((newr,newc))
            return visited 
        pacific_reachable = multi_bfs(pacific_starts)
        atlantic_reachable = multi_bfs(atlantic_starts)
        reachable_both = (pacific_reachable & atlantic_reachable)
        return list(reachable_both)
        