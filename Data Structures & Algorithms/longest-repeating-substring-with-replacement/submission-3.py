class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxf = longest = 0
        count = {}
        for i,ch in enumerate(s):
            count[ch] = 1 + count.get(ch, 0)
            maxf = max(maxf, count[ch])
            while (i-l+1)-maxf>k:
                count[s[l]]-=1
                l+=1
            longest = max(longest, i-l+1)
        return longest