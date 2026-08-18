class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0
        for i in nums:
            count = 1
            if i-1 not in hashSet:
                temp = i+1
                while temp in hashSet:
                    count+=1
                    temp+=1
            maxCount = max(maxCount, count)
        return maxCount
