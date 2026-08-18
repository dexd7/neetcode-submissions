class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for s in [1,2]:
                if (i-s)>=0:
                    dp[i] += dp[i-s]
        return dp[n]  