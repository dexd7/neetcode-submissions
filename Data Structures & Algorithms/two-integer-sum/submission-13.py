class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumChecker = {}
        for i, val in enumerate(nums):
            required = target - val
            if required in sumChecker:
                return [sumChecker[required],i]
            sumChecker[val] = i
        