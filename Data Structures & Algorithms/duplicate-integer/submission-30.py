class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dupli_checker = set()
        # for num in nums:
        #     if num in dupli_checker:
        #         return True
        #     dupli_checker.add(num)
        # return False

        # or
        return False if len(set(nums)) == len(nums) else True