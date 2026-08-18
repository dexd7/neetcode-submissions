class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxCount = 0
        for val in nums:
            count[val]+=1
            if count[val] > maxCount:
                maxVal = val
                maxCount = count[val]
        return maxVal
        

