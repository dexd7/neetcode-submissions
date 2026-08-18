class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                prevInd,prevTemp = stack.pop()
                res[prevInd] = ind-prevInd
            stack.append([ind,temp])
        return res
