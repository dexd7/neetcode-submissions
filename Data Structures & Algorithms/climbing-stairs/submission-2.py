class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in [1,2]:
                if i-j>=0:
                    dp[i] += dp[i-j]
        return dp[n] 