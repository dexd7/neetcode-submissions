class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(t)
        for c in s:
            if count[c] == 0:
                return False
            count[c]-=1
        return True