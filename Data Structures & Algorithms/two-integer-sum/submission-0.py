class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in table:
                return [table[result], i]
            table[num] = i
        return []
