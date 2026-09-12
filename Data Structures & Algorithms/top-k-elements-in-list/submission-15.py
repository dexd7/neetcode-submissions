from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counts = defaultdict(int)
        for num in nums:
            frequency_counts[num] += 1
        sorting_list = [[] for _ in range(len(nums)+1)]
        for number, count in frequency_counts.items():
            sorting_list[count].append(number)
        result = []
        for i in range(len(nums), 0, -1):
            while sorting_list[i]:
                result.append(sorting_list[i].pop())
                k-=1
                if k==0:
                    return result
            