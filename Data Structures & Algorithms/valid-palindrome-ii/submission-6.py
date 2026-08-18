class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<=r:
            if s[l] != s[r]:
                exclude_left = s[l+1:r+1]
                exclude_right = s[l:r]
                if exclude_left == exclude_left[::-1] or exclude_right == exclude_right[::-1]:
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True