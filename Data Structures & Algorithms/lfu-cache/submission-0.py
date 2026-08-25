class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {} # [value, frequency, timestamp]
        self.cap = capacity
        self.timestamp = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache[key][1] += 1
        self.timestamp +=1
        self.cache[key][2] = self.timestamp
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap<=0:
            return
        self.timestamp +=1
        if key in self.cache:
            self.cache[key][1] +=1
            self.cache[key][0] = value
            self.cache[key][2] = self.timestamp
            return
        if len(self.cache) >= self.cap:
            minimum_freq = float('inf')
            minimum_ts = float('inf')
            lfu = None
            for k, (_, freq, ts) in self.cache.items():
                if freq<minimum_freq or (freq == minimum_freq and ts<minimum_ts):
                    lfu = k
                    minimum_ts = ts
                    minimum_freq = freq
            if lfu is not None:
                del self.cache[lfu]
        self.cache[key] = [value, 1, self.timestamp]
                    


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)