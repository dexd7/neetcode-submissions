class TimeMap:

    def __init__(self):
        self.time_based_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_based_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_based_store[key]: return ''
        l = 0
        r = len(self.time_based_store[key])-1
        while l<=r:
            m = l+(r-l)//2
            if self.time_based_store[key][m][1] == timestamp:
                return self.time_based_store[key][m][0]
            if self.time_based_store[key][m][1]>timestamp:
                r = m-1
            else:
                l = m+1
        return '' if self.time_based_store[key][0][1]>timestamp else self.time_based_store[key][r][0]