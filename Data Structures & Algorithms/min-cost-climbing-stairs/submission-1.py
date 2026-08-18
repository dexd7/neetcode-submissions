class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we need to keep track of what steps are minimum costing to end if we start iterating from the end.
        # so basically we skip the last two index because they take us to the end guaranteed. Now we need to calculate
        # the minimum cost to the start of the array. In the end whatever is smaller out of index 0 or 1 will be the way
        # to go since we are allowed to start from both indexes.
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])