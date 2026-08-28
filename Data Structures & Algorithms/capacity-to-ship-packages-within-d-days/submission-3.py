class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #least weight we can ship with has to be max(weights) for sure
        #max weight we can ship with can be sum(weights) if we have to complete the delivery in one day
        def canShip(maxCapacity):
            curr_capacity = 0
            days_took = 1
            for weight in weights:
                if curr_capacity+weight>maxCapacity:
                    days_took+=1
                    curr_capacity = weight
                else:
                    curr_capacity+=weight
                if days_took>days:
                    return False
            return True
        l, r = max(weights), sum(weights) 
        
        while l<=r:
            weight_cap = l+(r-l)//2
            if canShip(weight_cap):
                r = weight_cap-1
            else:
                l = weight_cap+1
        return l