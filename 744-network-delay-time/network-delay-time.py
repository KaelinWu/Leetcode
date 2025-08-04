class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for time in times:
            u,v,w = time
            adj[u].append((v,w))

        minheap = [(0,k)]
        visited = set()
        res = 0
        while minheap:
            time,curr = heapq.heappop(minheap)
            if curr in visited:
                continue
            visited.add(curr)
            print(curr)
            for v,w in adj[curr]:
                if v not in visited:
                    heapq.heappush(minheap,(time+w,v))
            res = time
        print(visited)
        return res if len(visited) == n else -1

       
