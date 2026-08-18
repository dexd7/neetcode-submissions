class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buck = {}
        req = 0
        for i, num in enumerate(nums):
            req = target - num
            if num in buck:
                return [buck[num], i]
            buck[req] = i