class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_buck = {}
        for i, num in enumerate(nums):
            target_buck[target - num] = i
        for y, num in enumerate(nums):
            if num in target_buck:
                if y != target_buck[num]:
                    return [y, target_buck[num] ]
        return []