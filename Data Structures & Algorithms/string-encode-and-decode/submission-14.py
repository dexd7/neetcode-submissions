class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if not strs or strs == []:
            return ""
        for string in strs:
            res+=str(len(string))+"#"+string
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        answer = []
        j=0
        i=0
        while i<len(s):
            while(s[j]!="#"):
                j+=1
            length = int(s[i:j])
            answer.append(s[j+1:j+1+length])
            i = j+1+length
            j=i
        return answer
            