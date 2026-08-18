class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit  = 0
        for i in range(len(prices)-1):
            l = i + 1
            while l<len(prices):
                profit = max(profit, prices[l]-prices[i])
                l+=1
        return profit