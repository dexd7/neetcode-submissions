class StockSpanner:

    def __init__(self):
        self.stack = []
        
    
    def next(self, price: int) -> int:
        count = 1
        if not self.stack:
            self.stack.append((price, 1)) #1 here is span of the first item, since if today is the 
                                          #only day then span is 1
            return 1
        while self.stack and price>=self.stack[-1][0]:
            count+=self.stack.pop()[1]
        self.stack.append((price,count))
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)