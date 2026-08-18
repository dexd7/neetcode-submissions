class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = defaultdict(int)
        for truster,trustee in trust:
            trust_count[trustee] +=1
            trust_count[truster]-=1
        for i in range(n+1):
            if trust_count[i] == n-1:
                return i
        return -1