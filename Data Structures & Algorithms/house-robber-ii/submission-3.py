class Solution:
    def rob(self, nums: List[int]) -> int:
        #[3,4,2,4,5,6]->start of list
        #can't rob adjacent houses
        # max money.
        # we can either rob 1st house or last house.
        if len(nums) == 1:
            return nums[0]
        def maxLoot(money_count):
            curr,prev = 0,0
            for n in money_count:
                prev,curr = curr, max(curr, prev+n)
            return curr
        return max(maxLoot(nums[1:]),maxLoot(nums[:-1]))              