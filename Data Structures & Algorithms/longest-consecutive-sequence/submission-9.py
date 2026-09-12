class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        hashSet = set(nums)
        for num in nums:
            if num-1 not in hashSet:
                current_sequence = 1
                starter = num
                while starter+1 in hashSet:
                    starter+=1
                    current_sequence+=1
                longest_sequence = max(longest_sequence, current_sequence)
        return longest_sequence