class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #multi source BFS
        pacific_starts = deque()
        atlantic_starts = deque()
        ROWS, COLS = len(heights), len(heights[0])
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific_starts.append((r, c))
                if r == ROWS-1 or c == COLS-1:
                    atlantic_starts.append((r, c))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        #Input: the starting points
        #Output: set of all points in the grid from which water can flow to these starting points.
        def bfs(q):
            reachable = set(q)
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<ROWS and 0<=newc<COLS and (newr, newc) not in reachable and heights[newr][newc]>=heights[r][c]:
                        reachable.add((newr, newc))
                        q.append((newr, newc))
            return reachable
                        

        
        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)
        return list(pacific_reachable & atlantic_reachable)