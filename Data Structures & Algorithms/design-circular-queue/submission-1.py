class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.q_size = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.q_size:
            return False
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.q:
            return False
        self.q.pop(0)
        return True

    def Front(self) -> int:
        if not self.q:
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if not self.q:
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return self.q == []

    def isFull(self) -> bool:
        return self.q_size == len(self.q)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()