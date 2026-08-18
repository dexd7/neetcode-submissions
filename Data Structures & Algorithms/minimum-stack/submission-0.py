class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimumVal:
            self.minimumVal.append(min(self.minimumVal[-1], val))
        else:
            self.minimumVal.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minimumVal.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimumVal:
            return self.minimumVal[-1]

        
