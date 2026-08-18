class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        l = 0
        curr_sum = 0
        running_length = 0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            while curr_sum >= target:
                minLength=min(minLength, i-l+1)
                curr_sum-=nums[l]
                l+=1
        return minLength if minLength!=float('inf') else 0
        