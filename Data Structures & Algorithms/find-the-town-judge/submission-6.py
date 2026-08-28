class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge_candidates = {i: 0 for i in range(n+1)}
        for truster, trustee in trust:
            judge_candidates[truster]-=1
            judge_candidates[trustee]+=1
        for i in range(1,n+1):
            if judge_candidates[i] == n-1:
                return i
        return -1