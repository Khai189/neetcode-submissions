class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cur_span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, span = self.stack.pop()
            cur_span+=span
        
        self.stack.append((price, cur_span))

        return cur_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)