class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #maintaining heap of maximum counts and queue for remaining_instancese to another instance of the same element, and how many more instances are available
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)
        queue = deque() # (remaining_instances, count_left)
        instances = 0
        while heap or queue:
            instances += 1
            if queue and queue[0][0] == instances:
                heapq.heappush(heap, queue.popleft()[1])
            if heap:
                cnt = heapq.heappop(heap)
                cnt+=1
                if cnt:
                    queue.append((instances+n+1, cnt))
            #else we don't do anything (case for idle)
        return instances