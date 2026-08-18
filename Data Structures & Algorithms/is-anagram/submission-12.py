class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        counts = Counter(s)
        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        return True
