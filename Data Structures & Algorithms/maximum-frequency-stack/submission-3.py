class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.frequencies = [[]]

    def push(self, val: int) -> None:
        self.counter[val] += 1
        if self.counter[val] == len(self.frequencies):
            self.frequencies.append([])
        self.frequencies[self.counter[val]].append(val)
        
    def pop(self) -> int:
        val_deleted = self.frequencies[-1].pop()
        self.counter[val_deleted]-=1
        if not self.frequencies[-1]:
            self.frequencies.pop()
        return val_deleted


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()