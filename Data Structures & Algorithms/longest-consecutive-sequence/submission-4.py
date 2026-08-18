class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        for i in nums:
            if i-1 not in nums:
                running_sequence = 1
                temp = i
                while temp+1 in nums:
                    running_sequence+=1
                    temp+=1
                max_seq = max(max_seq, running_sequence)
        return max_seq
