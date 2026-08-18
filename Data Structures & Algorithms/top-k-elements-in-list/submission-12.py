class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        frequency = [[] for _ in range(len(nums)+1)]
        for num, cnt in count.items():
            frequency[cnt].append(num)
        res = []
        for i in range(len(frequency)-1,-1,-1):
            while frequency[i] and len(res)<k:
                res.append(frequency[i].pop())
            if len(res) == k:
                return res

            

            