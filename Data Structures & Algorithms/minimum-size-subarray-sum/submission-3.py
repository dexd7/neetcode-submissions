class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = pointer = 0
        mini = float('inf')
        for i, num in enumerate(nums):
            total+=num
            while total>=target:
                mini = min(mini, i-pointer+1)
                total-=nums[pointer]
                pointer+=1
        return 0 if mini==float('inf') else mini
