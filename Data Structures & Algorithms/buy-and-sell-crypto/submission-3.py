class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l = 0
        r = 1
        while l<r and r < len(prices):
            if prices[r]<prices[l]:
                l=r
                r=l+1
            else:
                max_p = max(max_p,prices[r]-prices[l])
                r+=1
        return max_p