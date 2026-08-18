class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0]<v:
                _,ind = stack.pop()
                result[ind] = i-ind
            stack.append([v,i])
        return result