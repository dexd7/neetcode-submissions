class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_to_origin = [[((x-0)**2 + (y-0)**2),x,y] for x, y in points]
        heapq.heapify(euclidean_to_origin)
        res = []
        while len(res)<k:
            point = heapq.heappop(euclidean_to_origin)
            res.append([point[1],point[2]])
        return res