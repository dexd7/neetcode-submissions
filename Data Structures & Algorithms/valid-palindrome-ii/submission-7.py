class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<=r:
            if s[l] != s[r]:
                skipLeftChar = s[l+1:r+1]
                skipRightChar = s[l:r]
                if skipLeftChar != skipLeftChar[::-1] and skipRightChar != skipRightChar[::-1]:
                    return False
            l+=1
            r-=1
        return True