class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Brute Force solution:
        #Time Complexity: O(n^2)
        maximum_number = max(nums)
        for i in range(1, abs(maximum_number)+1):
            if i not in nums:
                return i
        return maximum_number+1 if maximum_number>=0 else 1
