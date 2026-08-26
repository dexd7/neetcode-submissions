class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        best_k = float('inf')
        while l<=r:
            k = l+(r-l)//2
            time_taken = 0
            for pile in piles:
                time_taken+=math.ceil(pile/k)
            if time_taken<=h:
                best_k = min(best_k, k)
                r = k-1
            else:
                l = k+1
        return best_k