class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_starts = deque()
        atlantic_starts = deque()
        ROWS, COLS = len(heights), len(heights[0])
        for i in range(ROWS): # for the vertical rows
            pacific_starts.append((i, 0))
            atlantic_starts.append((i, COLS-1))
        for j in range(1, COLS): # for horizontal row of pacific starts
            pacific_starts.append((0, j))
        for j in range(COLS-1): # for horizontal row of atlantic starts
            atlantic_starts.append((ROWS-1, j))
        # directions water can flow in
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def bfs(queue):
            reachable = set(queue)
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    newr, newc = r+dr, c+dc
                    if 0<=newr<ROWS and 0<=newc<COLS and (newr, newc) not in reachable and heights[newr][newc]>=heights[r][c]:
                        reachable.add((newr, newc))
                        queue.append((newr, newc))
            return reachable
        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)
        
        return list(pacific_reachable & atlantic_reachable)