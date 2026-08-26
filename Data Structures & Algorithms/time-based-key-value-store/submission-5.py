class TimeMap:

    def __init__(self):
        self.storer = defaultdict(list) #key: List(value,timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storer[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.storer[key]: return ''
        l, r  = 0, len(self.storer[key])-1
        while l<=r:
            mid = l+(r-l)//2
            if self.storer[key][mid][1] == timestamp:
                return self.storer[key][mid][0]
            elif self.storer[key][mid][1]>timestamp:
                r = mid-1
            else:
                l = mid+1
        return '' if self.storer[key][0][1]>timestamp else self.storer[key][r][0]
            
            
