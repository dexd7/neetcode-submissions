class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for ind, val in enumerate(nums):
            requiredVal = target-val
            if requiredVal in bucket:
                return [bucket[requiredVal], ind]
            bucket[val] = ind
        return None
    