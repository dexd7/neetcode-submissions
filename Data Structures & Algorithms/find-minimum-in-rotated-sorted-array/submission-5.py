class Solution:
    def findMin(self, nums: List[int]) -> int:
        bot, top = 0, len(nums)-1
        res = nums[0]
        while bot<=top:
            if nums[bot]<nums[top]:
                return min(res,nums[bot])
            mid = (bot + top)//2
            res = min(res, nums[mid])
            if nums[mid]>=nums[bot]:
                bot = mid+1
            else:
                top = mid-1
        return res