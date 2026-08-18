class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashMap = { '2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz' }
        def dfs(i, currString):
            if len(currString) == len(digits):
                res.append(currString)
                return
            for ch in hashMap[digits[i]]:
                dfs(i+1, currString+ch)
        if digits:
            dfs(0, '')
        return res