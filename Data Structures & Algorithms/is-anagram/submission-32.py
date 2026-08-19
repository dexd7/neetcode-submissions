class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = Counter(s)
        for ch in t:
            if temp[ch]==0:
                return False
            temp[ch] -= 1
        return True