class StockSpanner:

    def __init__(self):
        self.price_history = [].remove()

    def next(self, price: int) -> int:
        current_span = 1

        while self.price_history and self.price_history[-1][0] <= price:
            previous_price, previous_span = self.price_history.pop()
            current_span += previous_span

        self.price_history.append((price, current_span))

        return current_span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)