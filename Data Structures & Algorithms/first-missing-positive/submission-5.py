class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Brute Force solution:
        #Time Complexity: O(n^2)
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i
        
