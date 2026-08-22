class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.frequencies = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        f = self.counter[val]
        self.maxFreq = f if f>self.maxFreq else self.maxFreq
        self.frequencies[f].append(val)
        
    def pop(self) -> int:
        val_deleted = self.frequencies[self.maxFreq].pop()
        self.counter[val_deleted] -= 1
        if not self.frequencies[self.maxFreq]:
            self.maxFreq -=1
        return val_deleted



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()