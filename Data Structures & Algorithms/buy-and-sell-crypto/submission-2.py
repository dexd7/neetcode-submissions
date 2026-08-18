class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        l = 0
        max_p = 0
        while r<len(prices):
            if prices[r]>prices[l]:
                max_p = max(max_p, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_p
        