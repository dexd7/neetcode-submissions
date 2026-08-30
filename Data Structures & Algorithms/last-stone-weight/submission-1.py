class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)
        while len(minHeap)>1:
            a = -heapq.heappop(minHeap)
            b = -heapq.heappop(minHeap)
            if a-b == 0:
                continue
            else:
                heapq.heappush(minHeap, -(a-b))
        return 0 if not minHeap else -minHeap[0]
