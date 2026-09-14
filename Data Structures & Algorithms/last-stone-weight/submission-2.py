class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-stone for stone in stones]
        heapq.heapify(minHeap)
        while len(minHeap)>1:
            heavier_stone = heapq.heappop(minHeap)
            lighter_stone = heapq.heappop(minHeap)
            heapq.heappush(minHeap, heavier_stone-lighter_stone)
        return -minHeap[0]