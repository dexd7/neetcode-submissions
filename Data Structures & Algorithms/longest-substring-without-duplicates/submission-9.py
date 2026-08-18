class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        checker = set()
        for i in s:
            if i not in checker:
                checker.add(i)
                longest = max(longest, len(checker))
            else:
                while i in checker:
                    checker.remove(s[l])
                    l+=1
                checker.add(i)
        return longest
                