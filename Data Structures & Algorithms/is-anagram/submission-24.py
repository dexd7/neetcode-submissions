class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(s)
        for ch in t:
            if count[ch] == 0:
                return False
            count[ch] -= 1
        return True