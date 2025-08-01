class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))

        minheap = [(0,k)]
        res = 0
        visited = set()
        while minheap:
            time,node = heapq.heappop(minheap)

            if node in visited:
                continue
            visited.add(node)
            res = time
            for edge in edges[node]:
                v,w = edge
                if v not in visited:
                    heapq.heappush(minheap,(w+time,v))
            
        print(visited)
        print(res)
        if len(visited) == n:
            return res
        return -1


       
