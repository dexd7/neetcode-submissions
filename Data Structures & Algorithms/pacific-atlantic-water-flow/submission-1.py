class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        pacific_starts = []
        for c in range(COLS):
            pacific_starts.append((0,c))
        for r in range(1,ROWS):
            pacific_starts.append((r,0))
        atlantic_starts = []
        for c in range(COLS):
            atlantic_starts.append((ROWS-1,c))
        for r in range(ROWS-1):
            atlantic_starts.append((r,COLS-1))
        def multi_bfs(starts):
            q = deque(starts)
            visited = set(starts)
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dx,dy in dirs:
                        nr,nc = r+dx,c+dy
                        if (0<=nr<ROWS and
                            0<=nc<COLS and
                            (nr,nc) not in visited and 
                            heights[nr][nc]>=heights[r][c]):
                            q.append((nr,nc))
                            visited.add((nr,nc))
            return visited

        pacific_reachable = multi_bfs(pacific_starts)
        atlantic_reachable = multi_bfs(atlantic_starts)
        return list(pacific_reachable & atlantic_reachable)
                
            