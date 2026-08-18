class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        l = 0
        max_p = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1
        return max_p
        # min_price = float('inf')  
        # max_profit = 0  
        
        # for price in prices:
        #     min_price = min(min_price, price)  
        #     max_profit = max(max_profit, price - min_price)  
            
        # return max_profit  