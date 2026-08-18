class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        return_string = ""
        for i in range(n):
            return_string+=str(len(strs[i]))+'#'+strs[i]
        return return_string

    def decode(self, s: str) -> List[str]:
        n = len(s)
        l = 0
        r = 0
        return_list = []
        while r<n:
            if s[r] != '#':
                r+=1
            else:
                length = int(s[l:r])
                return_list.append(s[r+1:r+1+length])
                l = r+1+length
                r = l+1
        return return_list