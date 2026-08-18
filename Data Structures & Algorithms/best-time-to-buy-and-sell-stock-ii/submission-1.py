class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0
        fast = 1
        profit = 0
        while slow<fast and fast<len(prices):
            if prices[fast]>prices[slow]:
                profit+=prices[fast]-prices[slow]
                slow+=1
                fast+=1
            else:
                slow = fast
                fast+=1
        return profit