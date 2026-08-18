class MinStack:

    def __init__(self):
        self.minStack = []
        self.lastMin = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.lastMin:
            self.lastMin.append(min(self.lastMin[-1], val))
        else:
            self.lastMin.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.lastMin.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.lastMin[-1]
