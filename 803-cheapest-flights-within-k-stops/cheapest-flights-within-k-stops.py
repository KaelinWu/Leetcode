class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        prices = [float("infinity")] * n
        prices[src] = 0
        for source, destination, price in flights:
            adj[source].append((price,destination))
        minheap = deque()
        minheap.append((0,0,src)) #price, k, src

        while minheap:
            price,stops,curr = minheap.popleft()
            if stops > k:
                continue
            for new_price, dest in adj[curr]:
                if new_price+price < prices[dest]:
                    prices[dest] = new_price +price
                    minheap.append((price+new_price,stops+1,dest))
        
        return prices[dst] if prices[dst] != float("infinity") else -1
