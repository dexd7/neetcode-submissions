class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = Counter(s)
        for ch in t:
            if ch in counts and counts[ch]>0:
                counts[ch]-=1
            else:
                return False
        return True