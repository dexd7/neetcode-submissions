class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            length = len(i)
            res+=str(length)+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        strs = []
        length = len(s)
        while i<length:
            while s[j] != "#":
                j+=1
            lent = int(s[i:j])
            strs.append(s[j+1:j+1+lent])
            i = j+1+lent
            j = i
        return strs
