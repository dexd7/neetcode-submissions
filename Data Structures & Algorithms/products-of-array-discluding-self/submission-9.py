class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = 1
        res = []
        for i in range(len(nums)):
            res.append(product_left)
            product_left*= nums[i]
        product_right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= product_right
            product_right*=nums[i]
        return res
