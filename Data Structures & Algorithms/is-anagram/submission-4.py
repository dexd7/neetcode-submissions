class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        set = {}
        for char in s:
            set[char] = set.get(char, 0) + 1
        for char in t:
            if char not in set or set[char] == 0:
                return False  
            set[char] -= 1  

        return True
        