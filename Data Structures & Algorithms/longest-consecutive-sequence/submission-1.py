class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 1
        max_c = 0
        for n in nums:
            count = 1
            if n-1 not in numSet:
                temp = n
                while temp+1 in numSet:
                    temp+=1
                    count+=1
            max_c = max(max_c,count)
        return max_c