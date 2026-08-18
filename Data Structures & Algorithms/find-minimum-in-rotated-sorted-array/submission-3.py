class Solution:
    def findMin(self, nums: List[int]) -> int:
        top = len(nums)-1
        bot = 0
        res = nums[0]
        while top>=bot:
            if nums[bot]<nums[top]:
                res = min(res, nums[bot])
                break
            mid = (top+bot)//2
            res = min(res,nums[mid])
            if nums[mid]<nums[bot]: #we are in right sorted portion so we want to move left
                top = mid-1
            else:
                bot = mid+1
        return res