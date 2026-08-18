class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        max_sequence = 0
        for i in nums:
            if i-1 not in hashSet:
                running_seq = 1
                temp = i
                while temp+1 in hashSet:
                    temp+=1
                    running_seq += 1
                max_sequence=max(max_sequence,running_seq)
        return max_sequence
