class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #[30,38,30,36,35,40,28] monotonically decreasing stack (non-strict)
        # so whenever we see a greater temperature value in the stack we pop and update input list.
        stack = [] # [index,temperature]
        res = [0]* len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]: # we have found a warmer day
                index, _ = stack.pop()
                res[index] = i-index
            stack.append([i,temperatures[i]])
        return res