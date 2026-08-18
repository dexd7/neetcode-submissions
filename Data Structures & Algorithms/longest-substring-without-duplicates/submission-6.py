class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterSet = set()
        l = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in letterSet:
                letterSet.remove(s[l])
                l+=1
            letterSet.add(s[i])
            ans = max(ans,len(letterSet))
        return ans