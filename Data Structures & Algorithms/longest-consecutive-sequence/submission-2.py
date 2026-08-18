class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        count = 1
        max_count = 0
        for i in nums:
            count = 1
            if i-1 not in num:
                temp = i
                while temp + 1 in num:
                    temp +=1
                    count+=1
            max_count = max(max_count, count)
        return max_count
