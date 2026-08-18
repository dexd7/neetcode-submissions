class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        res = []
        def dfs(opens, closes):
            if opens == closes == n:
                res.append(''.join(subset.copy()))
                return
            if opens<n:
                subset.append('(')
                dfs(opens+1,closes)
                subset.pop()
            if closes<opens:
                subset.append(')')
                dfs(opens, closes+1)
                subset.pop()
        dfs(0, 0)
        return res