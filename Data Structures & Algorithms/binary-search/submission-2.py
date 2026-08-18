class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top, bot = 0, len(nums)-1
        while top<=bot:
            mid = (top+bot)//2
            if nums[mid]>target:
                bot = mid-1
            elif nums[mid]<target:
                top = mid+1
            else:
                return mid
        return -1
        
        