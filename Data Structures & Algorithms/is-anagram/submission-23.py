class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lettercount = Counter(t)
        for ch in s:
            if ch in lettercount and lettercount[ch] != 0:
                lettercount[ch]-=1
            else:
                return False
        return True