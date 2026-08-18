class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i,num in enumerate(nums):
            need = target-num
            if need in temp:
                return [temp[need],i]
            temp[num]=i