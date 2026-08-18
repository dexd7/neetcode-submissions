class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            nums[pointer] = nums[i]
            pointer+=1
        return pointer