class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = Counter(t)
        for i in s:
            if not temp[i] or temp[i]== 0:
                return False
            temp[i]-=1
        return True
            