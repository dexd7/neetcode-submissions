class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<=r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return True if skipL == skipL[::-1] or skipR == skipR[::-1] else False
            l+=1
            r-=1
        return True