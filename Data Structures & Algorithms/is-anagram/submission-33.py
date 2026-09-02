class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if Counter(t) == Counter(s) else False