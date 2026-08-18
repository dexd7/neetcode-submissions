class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]]+=1
        frequency_map = defaultdict(list)
        for key,value in count.items():
            frequency_map[value].append(key)
        res = []
        for i in range(len(nums),-1,-1):
            while len(res)<k and frequency_map[i]:
                res.append(frequency_map[i].pop())
            if len(res) == k:
                return res