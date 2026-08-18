class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string)) + '*' + string
        return encoded_string
    def decode(self, s: str) -> List[str]:
        strs = []
        l = 0
        while l<len(s):
            r = l
            while s[r] != '*':
                r+=1
            length = int(s[l:r])
            l = r+1
            r += (length+1)
            strs.append(s[l:r])
            l = r
        return strs
