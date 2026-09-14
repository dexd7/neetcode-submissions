class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # euclidean_to_origin = [[((x-0)**2 + (y-0)**2),x,y] for x, y in points]
        # heapq.heapify(euclidean_to_origin)
        # res = []
        # while len(res)<k:
        #     point = heapq.heappop(euclidean_to_origin)
        #     res.append([point[1],point[2]])
        # return res
        # Second optimal approach prioritizing space complexity is as follows:
        heap = []
        for x,y in points:
            distance = -(x*x + y*y)
            heapq.heappush(heap, (distance,x,y))
            if len(heap)>k:
                heapq.heappop(heap)
        return [[x,y] for _,x,y in heap]    