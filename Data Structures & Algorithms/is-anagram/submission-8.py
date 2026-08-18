class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        track = Counter(s)
        for i in t:
            if i not in track or track[i] == 0:
                return False
            track[i] -=1
        return True
            
