class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    count+=1
                    ret.append(count)
                    break
                else:
                    if j == len(temperatures)-1:
                        ret.append(0)
                    else:
                        count +=1
        ret.append(0)
        return ret
