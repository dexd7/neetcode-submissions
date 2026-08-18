class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        majority_qualifier = len(nums)//3 + 1
        frequency = [[] for _ in range(len(nums)+1)]
        for num, cnt in count.items():
            frequency[cnt].append(num)
        res = []
        for i in range(len(nums),0,-1):
            while frequency[i] and i>=majority_qualifier:
               res.append(frequency[i].pop())
        return res 