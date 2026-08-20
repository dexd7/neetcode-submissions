class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        totalProfit = 0
        while l<r and r<len(prices):
            if prices[r]>prices[l]:
                totalProfit += prices[r]-prices[l]
                l+=1
            else:
                l=r
            r+=1
        return totalProfit