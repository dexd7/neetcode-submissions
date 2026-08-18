class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0,0,0]] #diff row col
        visited = set()
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] 
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r,c) == (ROWS-1, COLS-1):
                return diff
            for dx, dy in dirs:
                nr, nc = r+dx, c+dy
                if nr<0 or nr==ROWS or nc<0 or nc == COLS or (nr,nc) in visited:
                    continue
                newDiff = max(diff, abs(heights[nr][nc]-heights[r][c]))
                heapq.heappush(minHeap, [newDiff, nr, nc])
        

