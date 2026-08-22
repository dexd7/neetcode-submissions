class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer = 0
        res = ''
        while pointer<max(len(word1), len(word2)):
            if pointer<len(word1):
                res += word1[pointer]
            if pointer<len(word2):
                res += word2[pointer]
            pointer+=1
        return res
                
