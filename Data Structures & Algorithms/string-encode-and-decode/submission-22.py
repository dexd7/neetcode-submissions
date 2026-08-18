class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += str(len(strs[i]))+'#'+strs[i]
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded_list = []
        l = 0
        r = 0
        while r<len(s):
            if s[r]!='#':
                r+=1
            else:
                length = int(s[l:r])
                decoded_list.append(s[r+1:r+1+length])
                l = r+1+length
                r = l+1
        return decoded_list