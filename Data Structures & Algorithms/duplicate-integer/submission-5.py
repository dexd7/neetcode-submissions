class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = set()
        for i in nums:
            if i in num_count:
                return True
            num_count.add(i)
        return False