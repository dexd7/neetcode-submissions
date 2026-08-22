class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<=r:
            if s[l] != s[r]:
                skipL = s[l+1:r+1]
                skipR = s[l:r]
                return False if skipL != skipL[::-1] and skipR != skipR[::-1] else True
            l+=1
            r-=1
        return True