class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_starts = []
        atlantic_starts = []
        
        for i in range(COLS):
            pacific_starts.append((0,i))    
        for i in range(1,ROWS):
            pacific_starts.append((i,0))
        for j in range(ROWS):
            atlantic_starts.append((j, COLS-1))
        for j in range(COLS-1):
            atlantic_starts.append((ROWS-1, j))

        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        
        def bfs(starts):
            nonlocal dirs
            q = deque(starts)
            visited = set(starts)
            while q:
                r,c = q.popleft()
                for dy, dx in dirs:
                    nr = r+dx
                    nc = c+dy
                    if (0<=nr<ROWS and
                        0<=nc<COLS and
                        heights[nr][nc]>=heights[r][c] and
                        (nr,nc) not in visited):
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return visited

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)    
        
        return list(atlantic_reachable & pacific_reachable)