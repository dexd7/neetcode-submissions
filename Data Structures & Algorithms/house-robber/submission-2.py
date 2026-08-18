class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # if len(nums)==2:
        #     return max(nums)
        # for i in range(len(nums)-3,-1,-1):
        #     nums[i] = max(nums[i]+nums[i+2],nums[i+1])
        # return nums[0]
        curr,prev = 0,0
        for n in nums:
            curr,prev = max(curr,prev+n),curr
        return curr
