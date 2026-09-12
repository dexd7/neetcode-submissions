class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = Counter(t)
        for ch in s:
            if temp[ch] == 0:
                return False
            temp[ch]-=1
        return True