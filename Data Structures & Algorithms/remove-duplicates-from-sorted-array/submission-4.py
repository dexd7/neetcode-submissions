class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        for i in range(len(nums)):
            if temp and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
        nums[:] = temp
        return len(temp)