class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        dupli_check = set()
        for i in nums:
            if i in dupli_check:
                return True
            dupli_check.add(i)
            while len(dupli_check)>k:
                dupli_check.remove(nums[l])
                l+=1
        return False