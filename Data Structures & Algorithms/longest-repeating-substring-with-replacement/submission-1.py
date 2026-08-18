class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = l = maxf = 0
        count = {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            maxf = max(maxf, count[s[i]])
            while (i+1-l)-maxf>k:
                count[s[l]]-=1
                l+=1
            longest = max(longest, i-l+1)
        return longest
        