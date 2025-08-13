class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source, dest, price in flights:
            adj[source].append((price,dest))
        prices = [float("infinity")] * n

        que = deque()
        que.append((src,0,0))
        while que:
            curr, visits, price = que.popleft()
            print(curr)
            if visits > k:
                continue
            for new_price, dest in adj[curr]:
                if price + new_price < prices[dest]:
                    prices[dest] = price + new_price
                    que.append((dest,visits+1,prices[dest]))
        return prices[dst] if prices[dst] != float("infinity") else -1
