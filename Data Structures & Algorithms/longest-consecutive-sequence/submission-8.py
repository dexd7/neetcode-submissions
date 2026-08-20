class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0
        for num in nums:
            if num-1 not in hashSet: #then it is a true potential sequence starter
                count = 1
                while num+1 in hashSet:
                    count+=1
                    num+=1
                maxCount = max(maxCount, count)
        return maxCount