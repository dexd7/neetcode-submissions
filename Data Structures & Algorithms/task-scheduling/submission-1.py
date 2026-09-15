class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # #maintaining heap of maximum counts and queue for remaining_instancese to another instance of the same element, and how many more instances are available
        # counts = Counter(tasks)
        # heap = [-cnt for cnt in counts.values()]
        # heapq.heapify(heap)
        # queue = deque() # (remaining_instances, count_left)
        # instances = 0
        # while heap or queue:
        #     instances += 1
        #     if queue and queue[0][0] == instances:
        #         heapq.heappush(heap, queue.popleft()[1])
        #     if heap:
        #         cnt = heapq.heappop(heap)
        #         cnt+=1
        #         if cnt:
        #             queue.append((instances+n+1, cnt))
        #     #else we don't do anything (case for idle)
        # return instances
        #Greedy technique... whenever we have the maximum_frequency character:
        #Let's say max freq Character is A and max freq is 3 and n=2
        # then a proper layout possible would be [A..][A..][A] then the lower bound on the number of blocks like this that we need is ((maxfreq-1)*(n+1))+1 and if there were two maximum counts that were the same for example B existed with count 3 then it gets appended to the second position of the block each time and only the tail grows... so we tailor this equation accordingly: ((maxfreq-1)*(n+1))+count_of_maxfreq and finally if there were too many distinct elements, our idles would be 0 and so our cycle length at minimum would be length of tasks
        counts = Counter(tasks)
        maxFreq = max(counts.values())
        count_of_maxFreq = sum(1 for i in counts.values() if i==maxFreq)
        return max(len(tasks), ((maxFreq-1)*(n+1))+count_of_maxFreq)