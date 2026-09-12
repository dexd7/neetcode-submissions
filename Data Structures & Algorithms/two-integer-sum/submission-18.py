class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {} # value: index
        for ind, val in enumerate(nums):
            required = target-val
            if required in bucket:
                return [bucket[required], ind]
            bucket[val] = ind
        