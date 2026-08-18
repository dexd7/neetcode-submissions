class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(t)
        for ch in s:
            if ch not in count or count[ch] == 0:
                return False
            if ch in count and count[ch] != 0:
                count[ch]-=1
        return True