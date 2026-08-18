from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tracker = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tracker[key].append((value, timestamp))
                

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tracker:
            return ""
        bot = 0
        top = len(self.tracker[key])-1
        res = ""
        while bot<=top:
            mid = (bot+top)//2
            if self.tracker[key][mid][1]<=timestamp:
                res = self.tracker[key][mid][0]
                bot = mid + 1
            else:
                top = mid - 1
        return res



