class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        y = Counter(t)
        for char in s:
            if y[char] == 0 or char not in y:
                return False
            y[char]-=1
        return True