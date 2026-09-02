class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            pointer = 0
            while pointer<min(len(prefix),len(strs[i])) and prefix[pointer] == strs[i][pointer]:
                pointer+=1
            prefix = prefix[:pointer]
        return prefix