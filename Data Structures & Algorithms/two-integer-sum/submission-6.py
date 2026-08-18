class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_buck = {}
        need = 0
        for i,num in enumerate(nums):
            need = target - num
            if need in target_buck:
                return [target_buck[need], i]
            target_buck[num] = i
        return []
        