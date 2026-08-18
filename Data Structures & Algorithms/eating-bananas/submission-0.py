class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        top = max(piles)
        bot = 1
        res = float('inf')
        while bot<=top:
            k = (bot+top)//2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/k)
            if time_taken<=h:
                res = min(res, k)
                top = k-1
            else:
                bot = k+1
        return res