class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = float('inf')
        while l<=r:
            if nums[l]<nums[r]:
                return min(res, nums[l])
            mid = l+(r-l)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                res = min(res, nums[mid])
                r = mid-1
            

        return res
