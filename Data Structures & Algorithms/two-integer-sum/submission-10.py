class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i,v in enumerate(nums):
            required = target - v
            if  required in bucket:
                return [bucket[required], i]
            bucket[v] = i
        