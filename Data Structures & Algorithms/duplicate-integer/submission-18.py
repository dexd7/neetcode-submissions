class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupliChecker = set()
        for i in nums:
            if i in dupliChecker:
                return True
            dupliChecker.add(i)
        return False