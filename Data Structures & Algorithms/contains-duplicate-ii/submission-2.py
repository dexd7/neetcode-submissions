class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l = 0
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            if len(hashSet)==k:
                hashSet.remove(nums[l])
                l+=1
            hashSet.add(i)
        return False