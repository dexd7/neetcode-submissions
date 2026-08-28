class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return True
            if nums[l]==nums[mid]:
                l+=1
            elif nums[mid]<nums[r]:
                if nums[mid]>target or target>nums[r]:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid]>nums[l]:
                if nums[mid]<target or nums[l]>target:
                    l = mid+1
                else:
                    r = mid-1
            else:
                r = mid-1
            
        return False