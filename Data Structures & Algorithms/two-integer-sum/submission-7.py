class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        tg = 0
        for i,num in enumerate(nums):
            tg = target-num
            if num in bucket:
                return [bucket[num],i]
            bucket[tg] = i
        return []
