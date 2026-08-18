class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_bucket = {}
        for i,v in enumerate(nums):
            required = target-v
            if required in required_bucket:
                return [required_bucket[required], i]
            required_bucket[v] = i
        
        