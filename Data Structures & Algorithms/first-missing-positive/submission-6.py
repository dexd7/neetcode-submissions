class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # #Brute Force solution:
        # #Time Complexity: O(n^2)
        # for i in range(1, len(nums)+2):
        #     if i not in nums:
        #         return i
        
        # Second attempt at slightly optimal approach
        tracker = [False] * len(nums)
        for num in nums:
            if num>0 and num<=len(nums):
                tracker[num-1] = True
        for i in range(1, len(nums)+1):
            if not tracker[i-1]:
                return i
        return len(nums)+1
        