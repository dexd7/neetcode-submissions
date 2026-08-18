class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*(len(nums))
        post = 1
        for i,num in enumerate(nums):
            if i==0:
                output[i] = 1
            else:
                output[i] = nums[i-1]*output[i-1]
        for i in range(len(output)-1,-1,-1):
            output[i] = post*output[i]
            post = post*nums[i]
        return output