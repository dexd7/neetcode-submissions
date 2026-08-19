class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            pointer = 0
            while pointer<len(prefix):

                if pointer>=len(strs[i]) or (prefix[pointer] != strs[i][pointer]):
                    prefix = prefix[:pointer]
                    break
                pointer+=1
        return prefix