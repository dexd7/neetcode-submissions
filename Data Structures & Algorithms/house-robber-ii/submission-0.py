class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #house robber 1
        def house_robber1(nums):
            curr,prev = 0,0
            for n in nums:
                curr,prev = max(curr,prev+n),curr
            return curr
        return max(house_robber1(nums[1:]),house_robber1(nums[:-1]))