class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def isPalindrome(string):
            return string == string[::-1]
        def dfs(start):
            if start>=len(s):
                res.append(subset.copy())
                return
            for end in range(start, len(s)):
                potential = s[start:end+1]
                if isPalindrome(potential):
                    subset.append(potential)
                    dfs(end+1)
                    subset.pop()
        dfs(0)
        return res

