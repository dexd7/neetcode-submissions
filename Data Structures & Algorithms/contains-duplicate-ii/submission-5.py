class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sliding_window = set()
        l = 0
        for num in nums:
            if sliding_window and num in sliding_window:
                return True
            sliding_window.add(num)
            if len(sliding_window)>k:
                sliding_window.remove(nums[l])
                l+=1
        return False
