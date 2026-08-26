class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return True
            if nums[mid]>nums[l]:
                if target>nums[mid] or target<nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            elif nums[mid]<nums[l]:
                if target<nums[mid] or target>nums[r]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                l+=1
        return False