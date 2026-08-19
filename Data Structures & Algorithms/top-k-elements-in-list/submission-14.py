class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for i in nums:
            frequencies[i] = 1 + frequencies.get(i, 0)
        sortedArr = [[] for _ in range(len(nums)+1)]
        for val,count in frequencies.items():
            sortedArr[count].append(val)
        res = []
        for i in range(len(sortedArr)-1,0,-1):
            while k>0 and sortedArr[i]:
                res.append(sortedArr[i].pop())
                k-=1
            if k == 0:
                return res
                