class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = Counter(s)
        for i in t:
            if i in temp and temp[i] > 0:
                temp[i]-=1
            else:
                return False
        return True