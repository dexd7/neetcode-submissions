class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # euclidean_to_origin = defaultdict(list)
        # for x, y in points:
        #     euclidean_distance = math.sqrt((x - 0)**2 + (y - 0)**2)
        #     euclidean_to_origin[euclidean_distance].append([x,y])
        # minHeap = [distance for distance in euclidean_to_origin.keys()]
        # heapq.heapify(minHeap)
        # res = []
        # while k>0:
        #     curr_list = euclidean_to_origin[heapq.heappop(minHeap)]
        #     while curr_list and k>0:
        #         res.append(curr_list.pop())
        #         k-=1

        # return res

        #EASIER way: use tuple sorting
        minHeap = [[x*x+y*y, x, y] for x, y in points]
        heapq.heapify(minHeap)
        return [[x,y] for _,x,y in heapq.nsmallest(k, minHeap)]