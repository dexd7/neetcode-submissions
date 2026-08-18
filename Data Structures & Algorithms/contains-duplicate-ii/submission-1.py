class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
            if len(hashSet)>k:
                hashSet.remove(nums[l])
                l+=1
        return False