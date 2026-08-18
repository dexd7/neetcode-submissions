class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        frequency = [[] for _ in range(len(nums)+1)]
        for num,count in counts.items():
            frequency[count].append(num)
        res = []
        for i in range(len(frequency)-1,-1,-1):
            while len(res)<k and frequency[i]:
                res.append(frequency[i].pop())
        return res
