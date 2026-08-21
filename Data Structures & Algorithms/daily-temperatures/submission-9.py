class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempnind_tracker = []
        for i in range(len(temperatures)):
            while tempnind_tracker and tempnind_tracker[-1][0]<temperatures[i]:
                orig_index = tempnind_tracker.pop()[1]
                temperatures[orig_index] = i-orig_index
            tempnind_tracker.append((temperatures[i], i))
        for _,i in tempnind_tracker:
            temperatures[i] = 0
        return temperatures