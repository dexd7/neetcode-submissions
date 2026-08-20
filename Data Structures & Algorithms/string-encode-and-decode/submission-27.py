class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string  = ''
        for word in strs:
            encoded_string += (str(len(word)) + '*' + word)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        r = 1
        while r<len(s):
            while s[r] != '*':
                r+=1
            length = int(s[l:r])
            l = r+1
            r = l+length
            res.append(s[l:r])
            l = r
        return res
            
