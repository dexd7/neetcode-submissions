class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_bucket = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in target_bucket:
                return [target_bucket[result], i]
            target_bucket[num] = i
        return []