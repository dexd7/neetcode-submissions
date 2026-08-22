class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        pointer = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            nums[pointer] = nums[i]
            pointer+=1
        return pointer
