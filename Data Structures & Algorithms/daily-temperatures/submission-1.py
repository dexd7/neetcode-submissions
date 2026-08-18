class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                _ , index_of_last_element = stack.pop()
                res[index_of_last_element] = index - index_of_last_element
            stack.append([temp, index])
        return res

            



            

