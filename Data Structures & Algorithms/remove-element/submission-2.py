class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for num in nums:
            if num == val:
                continue
            nums[l] = num
            l+=1
        return l