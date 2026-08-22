class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding_window = set()
        longest_substring = 0
        pointer = 0
        for ch in s:
            while ch in sliding_window and pointer<len(s):
                sliding_window.remove(s[pointer])
                pointer+=1
            sliding_window.add(ch)
            longest_substring = max(longest_substring, len(sliding_window))
        return longest_substring