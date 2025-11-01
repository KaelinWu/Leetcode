class StockPrice:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.time_price = defaultdict(int)
        self.time = 0

    def update(self, timestamp: int, price: int) -> None:
        self.time_price[timestamp] = price

        heapq.heappush(self.minheap, (price,timestamp))
        heapq.heappush(self.maxheap, (-price,timestamp))
        if timestamp > self.time:
            self.time = timestamp
    def current(self) -> int:
        return self.time_price[self.time]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxheap[0]
            if self.time_price[timestamp] == -price:
                return -price
            else:

                heapq.heappop(self.maxheap)
    def minimum(self) -> int:
        while True:
            price, timestamp = self.minheap[0]
            if self.time_price[timestamp] == price:
                return price
            else:
                heapq.heappop(self.minheap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()