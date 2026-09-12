class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        cold_days = [] # [temperature, ind]
        res = [0] * len(temperatures) 
        for ind, temp in enumerate(temperatures):
            while cold_days and cold_days[-1][0]<temp:
                _, cold_ind = cold_days.pop()
                res[cold_ind] = ind-cold_ind
            cold_days.append([temp, ind])
        return res
        