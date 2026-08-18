class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                substring = s[i:j+1]
                
                #check for duplicate in current substring
                if len(set(substring)) == len(substring):
                    maxLen = max(maxLen, j-i+1)
        return maxLen