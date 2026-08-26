class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights),sum(weights) #can't split one package so lower bound should be maximum weight package. And in the worst case we could have to ship all packages in one day.
        def can_ship(cap): #Return True if this capacity can be used to ship all items.
            shipping_days = 1
            curr_cap = cap
            for w in weights:
                if curr_cap-w<0:
                    shipping_days+=1
                    if shipping_days>days:
                        return False
                    curr_cap = cap
                curr_cap-=w
            return True
        minimum_capacity = float('inf')            
        while l<=r:
            capacity = l+(r-l)//2
            if can_ship(capacity):
                minimum_capacity = min(minimum_capacity, capacity)
                r = capacity-1
            else:
                l = capacity+1
        return minimum_capacity
        

            