class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = defaultdict(int)
        self.frequencies = defaultdict(list)

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.stack.append(val)
        self.frequencies[self.counter[val]].append(val)
        
    def pop(self) -> int:
        val_deleted = 0
        for i in range(len(self.stack),0,-1):
            if self.frequencies[i]:
                val_deleted = self.frequencies[i].pop()
                self.counter[val_deleted] -= 1
                break
        return val_deleted




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()