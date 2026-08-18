class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]* len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][1]:
                ind,_ = stack.pop()
                res[ind] = i-ind
            stack.append((i, temperatures[i]))
        return res 