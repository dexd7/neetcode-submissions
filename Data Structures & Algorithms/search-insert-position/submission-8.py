class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)
    def binary_search(self, nums, l, r, target):
        if l>r:
            return l
        mid = l+((r-l)//2)
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            return self.binary_search(nums, mid+1, r, target)
        else:
            return self.binary_search(nums, l, mid-1, target)
    