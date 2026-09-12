class MinStack:

    def __init__(self):
        self.minStack = [] #[value, minimum of array with value included]

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append([val, val])
        else:
            self.minStack.append([val, min(self.minStack[-1][1], val)])

    def pop(self) -> None:
        if self.minStack: self.minStack.pop()

    def top(self) -> int:
        if self.minStack: return self.minStack[-1][0]

    def getMin(self) -> int:
        if self.minStack: return self.minStack[-1][1]
    
