class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        l = 0
        curr_sum = 0
        running_length = 0
        for i in range(len(nums)+1):
            while curr_sum >= target:
                minLength=min(minLength, running_length)
                curr_sum-=nums[l]
                l+=1
                running_length-=1
            if i!=len(nums):
                curr_sum+=nums[i]
                running_length+=1
        return minLength if minLength!=float('inf') else 0
        