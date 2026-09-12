class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_product = 1
        left_prods = []
        for num in nums:
            left_prods.append(running_product)
            running_product *= num
        running_product = 1
        for i in range(len(nums)-1, -1, -1):
            left_prods[i] *=running_product
            running_product *= nums[i]
        return left_prods