class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #house robber 1
        def house_robber1(l,r):
            curr,prev = 0,0
            for n in range(l,r+1):
                curr,prev = max(curr,prev+nums[n]),curr
            return curr
        return max(house_robber1(0,len(nums)-2),house_robber1(1,len(nums)-1))