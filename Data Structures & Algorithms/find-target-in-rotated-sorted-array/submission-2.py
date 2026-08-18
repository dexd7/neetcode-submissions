class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bot, top = 0, len(nums)-1
        while bot<=top:
            mid = (bot+top)//2
            if nums[mid] == target:
                return mid
            #left side
            if nums[mid]>=nums[bot]:
                if target>nums[mid] or target<nums[bot]:
                    bot = mid+1
                else:
                    top = mid-1
            #right side
            elif nums[mid]<=nums[top]:
                if target<nums[mid] or target>nums[top]:
                    top = mid-1
                else:
                    bot = mid+1
        return -1
