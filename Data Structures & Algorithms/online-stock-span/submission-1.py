class StockSpanner:

    def __init__(self):
        self.stack = []
        self.copy = []
    def next(self, price: int) -> int:
        
        counter = 1

        while self.copy and self.copy[-1] <= price:
            
            if counter == 1:
                self.copy = self.stack.copy()
            counter += 1
            self.copy.pop()
            
    
        self.stack.append(price)
        self.copy.append(price)
        return counter

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)